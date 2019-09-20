from collections import namedtuple

'''
A datatype defining either an array of qubits or classical bits.
These are defined in-program using the following syntax:
    (def blocka 1 2) # A two-qubit block using qubits one and two
    (def blockb 1 3) # Qubits 1-3
    (def blockc 1 2 classical) # Classical two-bit block for measurement
    (def blocka 1 2 quantum)   # Explicit syntax for two-qubit block
'''

Block = namedtuple('Block', ['start', 'end', 'type'])
Block.__new__.__defaults__ = ('quantum',)
Block.expand = lambda self : ' '.join(map(str, range(int(self.start), int(self.end))))
Block.__str__ = lambda self : self.expand()
