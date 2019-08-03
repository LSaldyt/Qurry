from .memory import Memory

class Kernel():
    def __init__(self, builder, size=64):
        self.memory = Memory(size)
        self.definitions = dict()
        self.builder = builder
