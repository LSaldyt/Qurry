from ..datatypes.block import Block

from .collect import collect
from .expand  import expand

from .CU import CU

def simU(block, target, unitary, unitary_block, kernel=None):
    '''
    Entangle multiple qubits, sequentially.
    '''
    code = []
    if not isinstance(block, Block):
        block = kernel.definitions[block]
    code.append(collect(block, target, kernel=kernel))
    code.append(CU(unitary, unitary_block, target, kernel=kernel))
    code.append(expand(block, target, kernel=kernel))
    return code
