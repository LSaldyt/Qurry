from ..utils import named_uuid

def map(operator, blockname, definitions=None):
    '''
    Apply a single-qubit operator to every qubit in a block
    (map H blocka)
    '''
    if definitions is None:
        definitions = dict()
    try:
        block = definitions[blockname]
    except KeyError:
        raise ValueError('The block {} is not defined'.format(blockname))
    return '\n'.join('{} {}'.format(operator, i)
            for i in range(block.start, block.end + 1))
