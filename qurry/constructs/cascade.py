from ..datatypes.block import Block

def cascade(block, kernel=None):
    '''
    Entangle multiple qubits, sequentially.
    '''
    code = ''
    if not isinstance(block, Block):
        block = kernel.definitions[block]
    for i in range(block.start, block.end - 1):
        code += 'CNOT {} {}\n'.format(i, i + 1)
    return code
