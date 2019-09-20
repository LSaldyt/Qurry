from collections import namedtuple

'''
A datatype defining a structured collection (kv map) of qubits or classical bits.
These are defined in-program using the following syntax:
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

class Instance(namedtuple('Instance', ['typename', 'data', 'mapping'])):
    __slots__ = ()
    def __new__(cls, typename, data, mapping=None):
        return super(Instance, cls).__new__(cls, typename, data, mapping)

class Datatype(namedtuple('Datatype', ['fields'])):
    __slots__ = ()
    def __new__(cls, fields=None, qubitmap=None):
        fields = dict() if fields is None else fields
        return super(Datatype, cls).__new__(cls, fields)

    def instance(cls, typename, *args, kernel=None, memmap=None):
        assert kernel is not None, 'Must initialize new structures with a valid kernel (got None)'
        assert memmap is not None, 'Failed to allocate memory for ({} {})'.format(typename, ' '.join(args))
        n = len(args)
        assert n % 2 == 0, 'Instance creation requires even number of arguments'
        m = n // 2
        keys   = [item for i, item in enumerate(args) if i % 2 == 0]
        values = [item for i, item in enumerate(args) if i % 2 == 1]

        data = dict()
        for key, value in zip(keys, values):
            assert value in kernel.definitions, '{} is undefined'.format(value)
            data[key] = kernel.definitions[value]
        return Instance(typename, data, memmap)

