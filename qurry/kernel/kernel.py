from .memory import Memory

class Kernel():
    def __init__(self, builder, topology):
        self.memory = Memory(topology.size)
        self.definitions = dict()
        self.builder = builder

    def define(self, name, value):
        if name in self.definitions:
            raise ValueError('{} is already defined'.format(name))
        else:
            self.definitions[name] = value
