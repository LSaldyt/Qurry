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
