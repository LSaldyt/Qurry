from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil

import numpy as np

from math import acos, sqrt, log, ceil, floor

from .controlled import bernoulli

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
        return [weights[0], []]

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
    for item in zip(first_tree, second_tree):
        item = list(item)
        levels.append(flatten(item))

    return [first_s, levels]

def write_diag_bernoulli_code(probtree, offset):
    code = ''
    for i, level in enumerate(probtree):
        level = [2 * acos(sqrt(x)) for x in level]
        n_qubits = floor(log(len(level), 2)) + 1
        code += '\nCRX_diag_{}({}) {}'.format(n_qubits,
                                              ', '.join(map(str, level)),
                                               ' '.join(map(str, (offset + n for n in range(n_qubits)))))
    return code

def multinomial(*weights, offset, definitions):
    weights = list(weights)
    print(len(weights))
    n_qubits = ceil(log(len(weights), 2))
    lendiff  = 2 ** n_qubits - len(weights)
    weights  = weights + [0] * lendiff

    initial_p, probtree = produce_probability_tree(weights)
    print(initial_p, probtree)

    code = ''
    for i in range(1, 4):
        code += CRX_diags(i)
    code += bernoulli(initial_p, offset)
    code += write_diag_bernoulli_code(probtree, offset)

    return code
