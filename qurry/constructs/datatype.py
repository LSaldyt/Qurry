from ..utils import named_uuid
from ..datatype import Datatype
from ..block import Block

# Eventually support classical types, but no need just yet
# types = {'bit', 'bits', 'qubit', 'qubits'}
types = {'qubit', 'qubits'}

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
        if isinstance(kind, list):
            assert kind[0] == 'block' and len(kind) == 3
            _, size, kind = kind
            dtype.fields[field_name] = Block(0, int(size), kind)
        else:
            assert kind in types, 'Data field ({} {}) does not use a valid type'.format(*field)
            dtype.fields[field_name] = kind
    if name in definitions:
        raise ValueError('Redefinition of {}'.format(name))
    definitions[name] = dtype
    return ''
