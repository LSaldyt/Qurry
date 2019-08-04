from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil

import numpy as np

from math import acos, sqrt, log, ceil, floor, erf
import sys, time

from .controlled import bernoulli

'''
A function and its helpers that define how to produce a multinomial distribution on a quantum computer.
Uses the "pick sticks?" method:
    Starting with probability 1 of state 0, split the state into two states of different probabilities using a rotation.
    Repeat this until all states are represented.
    For example:
        1.0
        |   \
        0.5  0.5 -----
        |   \     \   \
        0.25 0.25 0.25 0.25

    Or a non-uniform distribution:
        1.0
        |   \
        0.8  0.2 -----
        |   \     \   \
        0.2  0.6 0.15 0.05
'''

def flatten(l):
    if isinstance(l, list) and l and isinstance(l[0], list):
        return flatten([subitem for sublist in l for subitem in sublist])
    else:
        return l

def X(theta):
    return np.array([[quil_cos(theta / 2), -1j * quil_sin(theta / 2)], [-1j * quil_sin(theta / 2), quil_cos(theta / 2)]])

def CRX_diags(n):
    M = np.identity(2 ** n).astype(object)
    parameters = [Parameter('p' + str(i)) for i in range(2 ** (n - 1))]
    for i, p in enumerate(parameters):
        M[2*i:2*(i+1), 2*i:2*(i+1)] = X(p)
    CRX_diag = DefGate('CRX_diag_{}'.format(n), M, parameters)
    return str(CRX_diag)

def controlled_diag_bernoulli(weights, qubits):
    weights = [2 * acos(sqrt(w)) for w in weights]
    return CRX_diags(len(weights)) + '\n' + 'CRX_diag_{}({}) {}'.format(len(weights), ', '.join(weights), ' '.join(qubits))

def produce_probability_tree(weights):
    if len(weights) <= 2:
        return [[weights[0]]]

    n_qubits = ceil(log(len(weights), 2))
    divider  = 2 ** (n_qubits - 1)

    first        = weights[:divider]
    second       = weights[divider:]
    first_s      = sum(first)
    second_s     = sum(second)
    first_fracs  = [w / max(1e-8, first_s)  for w in first]
    second_fracs = [w / max(1e-8, second_s) for w in second]

    first_tree  = produce_probability_tree(first_fracs)
    second_tree = produce_probability_tree(second_fracs)

    levels = []
    for a, b in zip(first_tree, second_tree):
        levels.append(a + b)

    return [[first_s]] + levels

def write_diag_bernoulli_code(probtree, offset):
    code = ''
    for i, level in enumerate(probtree):
        if level:
            level = [2 * acos(sqrt(x)) for x in level]
            n_qubits = ceil(log(len(level), 2)) + 1
            code += '\nCRX_diag_{}({}) {}'.format(n_qubits,
                                                  ', '.join(map(str, level)),
                                                   ' '.join(map(str, (offset + n for n in range(n_qubits)))))
    return code

def multinomial(*weights, offset, definitions=None):
    print(offset)
    print(definitions)
    print(weights)
    weights = list(weights)
    block = definitions[offset]
    initial = block.start
    final = block.end
    #initial, *mid, final = definitions[offset].split(' ')
    assert int(final) - int(initial) <= len(weights)
    offset = int(initial)
    n_qubits = ceil(log(len(weights), 2))
    lendiff  = 2 ** n_qubits - len(weights)
    weights  = weights + [0.0] * lendiff

    initial_p, *probtree = produce_probability_tree(weights)
    initial_p = initial_p[0]

    code = ''
    for i in range(1, 8):
        code += CRX_diags(i)
    code += bernoulli(initial_p, offset)
    code += write_diag_bernoulli_code(probtree, offset)

    return code

def phi_normal(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def to_multinomial(a, b, n, phi):
    assert n >= 3, 'Minimum three discrete divisions required'
    n -= 2
    step  = (b - a) / n
    return discrete_multinomial_probabilities(a, b, step, phi)

def discrete_multinomial_probabilities(a, b, step, phi):
    probabilities = []
    i = a
    while i < b:
        probabilities.append(phi(i) - sum(probabilities))
        i += step
    probabilities.append(phi(b) - sum(probabilities))
    probabilities.append(phi(float('inf')) - sum(probabilities))
    return probabilities
