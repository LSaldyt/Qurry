from ..datatypes import update_definitions
from ..datatypes import Datatype

from pprint import pprint

def process_type(body, kernel):
    if len(body) == 1:
        body = body[0]
    head, *rest = body
    if head in kernel.definitions:
        dtype = kernel.definitions[head]
        assert isinstance(dtype, Datatype), 'The type {} is not a valid Datatype'.format(head)
        return dtype.instance(head, *rest, kernel=kernel, memmap=kernel.memory.allocate(dtype))
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
