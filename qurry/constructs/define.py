from ..definitions import update_definitions
from ..datatype import Datatype

from pprint import pprint

def process_type(body, definitions, builder):
    if len(body) == 1:
        body = body[0]
    head, *rest = body
    if head in definitions and isinstance(definitions[head], Datatype):
        return definitions[head].__init__(*rest)
    else:
        raise ValueError('Cannot process type {}'.format(head))

def define(*expression, definitions=None, builder=None):
    name, *rest = expression
    if name not in definitions:
        definitions[name] = process_type(rest, definitions, builder)
        pprint(definitions)
    else:
        raise ValueError('{} is already defined'.format(name))
    return ''
