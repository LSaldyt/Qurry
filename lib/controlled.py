from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil

import numpy as np

def controlled(U):
    base = np.identity(4).astype(complex)
    base[2:4,2:4] = np.array([[0, 1], [1, 0]])
    base[2:4,2:4] = U
    return base

Y = np.array([[0, 0.0-1j], [0.0+1j, 0]])
print(Y)
print(controlled(Y))

def controlled_X(n):
    theta = Parameter('theta')
    crx = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, quil_cos(theta / 2), -1j * quil_sin(theta / 2)], [0, 0, -1j * quil_sin(theta / 2), quil_cos(theta / 2)]])
    CRX = DefGate('CRX', crx, [theta])
    print(CRX)
    return CRX.get_constructor()(n)(0, 1)

print(controlled_X(1.567))
