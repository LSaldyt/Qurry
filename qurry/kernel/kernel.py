from .memory import Memory

class Kernel():
    def __init__(self, builder, topology):
        self.memory = Memory(topology.size)
        self.definitions = dict()
        self.builder = builder
