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

class Datatype(namedtuple('Datatype', ['fields', 'qubitmap'])):
    __slots__ = ()
    def __new__(cls, fields=None, qubitmap=None):
        fields = dict() if fields is None else fields
        qubitmap = dict() if qubitmap is None else qubitmap
        return super(Datatype, cls).__new__(cls, fields, qubitmap)
