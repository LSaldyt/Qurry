from ..datatypes.block import Block

def collect(block, target, kernel=None):
    '''
    Entangle multiple qubits, sequentially.
    '''
    code = []
    if not isinstance(block, Block):
        block = kernel.definitions[block]
    for i in range(block.start, block.end - 1):
        code.append(['CNOT', i, target])
    return code
