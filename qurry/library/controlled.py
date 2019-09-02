from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil

import numpy as np

from math import acos, sqrt

'''
Small helper functions that define common controlled gates.
Should be familiar to anyone if quantum computation.
The only new part is the "Bernoulli" gate, which is just an RX rotation meant to produce a classical state
'''

def controlled(U):
    base = np.identity(4).astype(complex)
    base[2:4,2:4] = np.array([[0, 1], [1, 0]])
    base[2:4,2:4] = U
    return base

def controlled_i(U):
    base = np.identity(4).astype(complex)
    base[2:4,2:4] = U
    base[2:4,2:4] = np.array([[0, 1], [1, 0]])
    return base

def bernoulli(p, q, rot='RX'):
    if p < 0:
        raise Warning('Bernoulli was called with negative probability: {}'.format(p))
    theta = 2 * acos(sqrt(abs(p)))
    return '{rot}({theta}) {q}'.format(rot=rot, theta=theta, q=q)

def controlled_X(n, a, b):
    theta = Parameter('theta')
    crx = controlled(np.array([[quil_cos(theta / 2), -1j * quil_sin(theta / 2)], [-1j * quil_sin(theta / 2), quil_cos(theta / 2)]]))
    CRX = DefGate('CRX', crx, [theta])
    return str(CRX) + '\n' + str(CRX.get_constructor()(n)(a, b))

def controlled_i_X(n, a, b):
    theta = Parameter('theta')
    cirx = controlled_i(np.array([[quil_cos(theta / 2), -1j * quil_sin(theta / 2)], [-1j * quil_sin(theta / 2), quil_cos(theta / 2)]]))
    CIRX = DefGate('CIRX', cirx, [theta])
    return str(CIRX) + '\n' + str(CIRX.get_constructor()(n)(a, b))

def controlled_bernoulli(n, a, b):
    theta = 2 * acos(sqrt(n))
    return controlled_X(theta, a, b)

def controlled_i_bernoulli(n, a, b):
    theta = 2 * acos(sqrt(n))
    return controlled_i_X(theta, a, b)
