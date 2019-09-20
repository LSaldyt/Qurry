from .memory import Memory
import uuid

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

    def named_uuid(self, name):
        # Create a named label, which is very useful in jump instructs and other control-flow
        return '{}-{}'.format(name, str(uuid.uuid4()))

