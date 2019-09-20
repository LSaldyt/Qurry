from ..datatypes import Datatype, Block

from .block import block

def process_type(body, kernel):
    if len(body) == 1:
        body = body[0]
    head, *rest = body
    if head in kernel.definitions:
        defined = kernel.definitions[head]
        assert isinstance(defined, Datatype), '{} is not a valid Datatype'.format(defined)
        return defined.instance(head, *rest, kernel=kernel, memmap=kernel.memory.allocate(defined)[0])
    elif head == 'block':
        return block(*rest, kernel=kernel)
    else:
        try:
            return kernel.builder(body, kernel)
        except:
            raise ValueError('Cannot process type {}'.format(head))

def define(*expression, kernel=None):
    name, *rest = expression
    kernel.define(name, process_type(rest, kernel))
    return ''
