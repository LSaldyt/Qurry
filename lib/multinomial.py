from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil

import numpy as np

from math import acos, sqrt

def X(theta):
    return np.array([[quil_cos(theta / 2), -1j * quil_sin(theta / 2)], [-1j * quil_sin(theta / 2), quil_cos(theta / 2)]])

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def CRX_diags(n):
    M = np.identity(2 ** n).astype(object)
    parameters = [Parameter(alphabet[i]) for i in range(2 ** (n - 1))]
    for i, p in enumerate(parameters):
        M[2*i:2*(i+1), 2*i:2*(i+1)] = X(p)
    CRX_diag = DefGate('CRX_diag_{}'.format(n), M, parameters)
    return str(CRX_diag)

#CRX_diags(1)
#CRX_diags(2)
#CRX_diags(3)
#CRX_diags(4)
#1/0
