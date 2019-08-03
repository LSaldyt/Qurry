from ..datatypes.block import Block

class Memory:
    '''
    A dirt-simple quantum memory tracker that literally breaks up an array of qubits and tracks which are used.
    Qubits are always allocated contiguously, and it is assumed they are never de-allocated
    '''
    def __init__(self, size):
        self.head = 0
        self.size = size

    def _inner_allocate(self, nqubits):
        if self.head + nqubits < self.size:
            offset = self.head + 1
            self.head += nqubits
        else:
            MemoryError('Cannot allocate more than {} qubits'.format(self.size))
        return offset

    def allocate(self, datatype):
        qubitmap = dict()
        nqubits = 0
        for field, fieldtype in datatype.fields.items():
            if isinstance(fieldtype, Block):
                block = fieldtype
                qubitmap[field] = nqubits
                nqubits += block.end - block.start
            elif fieldtype == 'qubit':
                qubitmap[field] = nqubits
                nqubits += 1
        offset = self._inner_allocate(nqubits)
        qubitmap = {k : offset + v for k, v in qubitmap.items()}
        return qubitmap


