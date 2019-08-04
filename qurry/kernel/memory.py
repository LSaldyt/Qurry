from ..datatypes.block import Block

from pprint import pprint

class Memory:
    '''
    A dirt-simple quantum memory tracker that literally breaks up an array of qubits and tracks which are used.
    Qubits are always allocated contiguously, and it is currently assumed they are never de-allocated
    '''
    def __init__(self, size):
        self.head = 0
        self.size = size

    def _inner_allocate(self, nqubits):
        begin = self.head
        if self.head + nqubits + 1 < self.size:
            offset = self.head + nqubits
            self.head += nqubits
        else:
            MemoryError('Cannot allocate more than {} qubits'.format(self.size))
        return Block(begin, offset)

    def allocate(self, datatype):
        qubitmap = dict()
        for field, fieldtype in datatype.fields.items():
            if isinstance(fieldtype, Block):
                block = fieldtype
                nqubits = block.end - block.start
            elif fieldtype == 'qubit':
                nqubits = 1
            qubitmap[field] = self._inner_allocate(nqubits)
        #print('Preallocation map:')
        #pprint(qubitmap)
        return qubitmap


