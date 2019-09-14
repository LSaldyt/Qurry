from ..datatypes.block import Block

from .CU import CU
from .reverseCascade import reverseCascade

def reverseCascadeU(block, unitary, unitary_block, kernel=None):
    '''
    Entangle multiple qubits, sequentially.
    '''
    if not isinstance(block, Block):
        block = kernel.definitions[block]
    code = reverseCascade(block, kernel=kernel)
    code += CU(unitary, unitary_block, block.start, kernel=kernel)
    return code
