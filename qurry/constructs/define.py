from ..definitions import update_definitions
from ..datatype import Datatype

from pprint import pprint

def process_type(body, kernel):
    if len(body) == 1:
        body = body[0]
    head, *rest = body
    if head in kernel.definitions and isinstance(kernel.definitions[head], Datatype):
        return kernel.definitions[head].__init__(*rest)
    else:
        raise ValueError('Cannot process type {}'.format(head))

def define(*expression, kernel=None):
    name, *rest = expression
    if name not in definitions:
        definitions[name] = process_type(rest, kernel)
    else:
        raise ValueError('{} is already defined'.format(name))
    return ''
