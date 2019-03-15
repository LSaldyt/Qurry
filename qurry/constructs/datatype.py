from ..utils    import named_uuid
from ..datatype import Datatype
from ..block    import Block
from ..memory   import Memory

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
    dtype = Datatype(dict(), dict())
    if definitions is None:
        definitions = dict()
    for field in fields:
        field_name, kind = field
        if isinstance(kind, list):
            assert kind[0] == 'block'
            dtype.fields[field_name] = Block(0, int(kind[1]), *kind[2:])
        else:
            assert kind in types, 'Data field ({} {}) does not use a valid type'.format(*field)
            dtype.fields[field_name] = kind
    if name in definitions:
        raise ValueError('Redefinition of {}'.format(name))
    memory = Memory(64)
    dtype.qubitmap.update(memory.allocate(dtype))
    definitions[name] = dtype
    return ''
