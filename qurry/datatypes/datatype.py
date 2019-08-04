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
        return super(Instance, cls).__new__(cls, typename, dict(), mapping)
    pass

class Datatype(namedtuple('Datatype', ['fields', 'qubitmap'])):
    __slots__ = ()
    def __new__(cls, fields=None, qubitmap=None):
        fields = dict() if fields is None else fields
        qubitmap = dict() if qubitmap is None else qubitmap
        return super(Datatype, cls).__new__(cls, fields, qubitmap)

    def instance(cls, typename, *args):
        data = dict()
        for key, value in zip(cls.fields.keys(), args):
            data[key] = value
        return Instance(typename, data, None)

