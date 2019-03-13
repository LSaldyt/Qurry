from ..utils import named_uuid
from ..datatype import Datatype

def datatype(name, *fields, definitions=None, builder=None):
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
    dtype = Datatype(dict())
    if definitions is None:
        definitions = dict()
    for field in fields:
        field_name, kind = field
        dtype.fields[field_name] = kind
    if name in definitions:
        raise ValueError('Redefinition of {}'.format(name))
    definitions[name] = dtype
    return ''
