from .cascade import cascade
from .CU import CU

def cascadeU(block, unitary, unitary_block, kernel=None):
    '''
    Entangle multiple qubits, sequentially.
    '''
    block = kernel.definitions[block]
    code = cascade(block, kernel=kernel)
    code += CU(unitary, unitary_block, block.end - 1, kernel=kernel)
    return code
