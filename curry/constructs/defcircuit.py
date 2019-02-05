from ..utils import named_uuid
from collections import namedtuple

Circuit = namedtuple('Circuit', ['arguments', 'expressions'])

def defcircuit(name, argdef, expressions, definitions=None, builder=None):
    '''
    Create a repeatable circuit
    '''
    circuit = Circuit(argdef, expressions)

    def circuit_builder(*args):
        return '\n'.join(builder(expr) for expr in expressions)

    definitions[name] = circuit_builder
    return '# This line defines the {} circuit'.format(name)
