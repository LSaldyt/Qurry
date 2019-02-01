from ..utils import named_uuid

def datatype(name, *fields, definitions=None):
    '''
    Define a qubit-based datatype
    i.e.
    (datatype my-datatype
        (a qubit)
        (b qubit)
        (c (block 3)))

    or perhaps implicitly

    (datatype my-datatype
        (a)
        (b)
        (c 3))
    '''
    if definitions is None:
        definitions = dict()
    return ''
