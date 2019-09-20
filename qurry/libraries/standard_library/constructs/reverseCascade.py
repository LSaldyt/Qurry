from ..datatypes.block import Block

def reverseCascade(block, kernel=None):
    '''
    Entangle multiple qubits, sequentially.
    '''
    code = ''
    if not isinstance(block, Block):
        block = kernel.definitions[block]
    for i in reversed(range(block.start, block.end - 1)):
        code += 'CNOT {} {}\n'.format(i + 1, i)
    return code
