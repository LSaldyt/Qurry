from ..datatypes.block import Block

def reverseCascade(block, kernel=None):
    '''
    Entangle multiple qubits, sequentially.
    '''
    code = []
    if not isinstance(block, Block):
        block = kernel.definitions[block]
    for i in reversed(range(block.start, block.end - 1)):
        code.append(['CNOT', i + 1, i])
    return code
