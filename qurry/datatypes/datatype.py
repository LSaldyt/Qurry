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

Datatype = namedtuple('Datatype', ['fields', 'qubitmap'])
