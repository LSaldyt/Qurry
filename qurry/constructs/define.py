from ..datatypes import update_definitions
from ..datatypes import Datatype, Block

from pprint import pprint

def process_type(body, kernel):
    if len(body) == 1:
        body = body[0]
    head, *rest = body
    if head in kernel.definitions:
        defined = kernel.definitions[head]
        assert isinstance(defined, Datatype), '{} is not a valid Datatype'.format(defined)
        return defined.instance(head, *rest, kernel=kernel, memmap=kernel.memory.allocate(dtype)[0])
    elif head == 'block':
        assert len(rest) > 0
        first = rest[0]
        rest  = rest[1:]
        defined = Block(0, int(first) + 1, *rest)
        _, defined = kernel.memory.allocate(defined)
        return defined
    else:
        raise ValueError('Cannot process type {}'.format(head))

def define(*expression, kernel=None):
    name, *rest = expression
    if name not in kernel.definitions:
        kernel.definitions[name] = process_type(rest, kernel)
        print('Kernel definitions:')
        pprint(kernel.definitions)
    else:
        raise ValueError('{} is already defined'.format(name))
    return ''
