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
    code.extend(collect(block, target, kernel=kernel))
    code.extend(CU(unitary, unitary_block, target, kernel=kernel))
    code.extend(expand(block, target, kernel=kernel))
    return code
