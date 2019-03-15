class Memory:
    '''
    A dirt-simple quantum memory tracker that literally breaks up an array of qubits and tracks which are used.
    Qubits are always allocated contiguously (to have a hope of mapping onto a real topology), and it is assumed they are never de-allocated
    '''
    def __init__(self, size):
        self.head = 0
        self.size = size

    def allocate(self, nqubits):
        if self.head + nqubits < self.size:
            self.head += nqubits
        else:
            MemoryError('Cannot allocate more than {} qubits'.format(self.size))

    def allocate(self, datatype):
        for field, fieldtype in datatype.fields.items():

