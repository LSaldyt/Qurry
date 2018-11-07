import sys

from pprint import pprint

from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES

from .utils import named_uuid
from .definitions import update_definitions

from . import constructs

from math import acos, asin, sin, cos, sqrt

def build(stack, definitions=None):
    print(stack)
    if definitions is None:
        definitions = dict()

    def replace_defs(code):
        for item, block in definitions.items():
            code = code.replace(item, block.expand())
        return code

    for expression in stack:
        assert len(expression) > 0, 'Error: parsed empty list {}'.format(expression)
        expression = ['\n'.join(build([item], definitions)) if isinstance(item, list) else item for item in expression]
        head = expression[0]
        upper = head.upper()
        if upper in STANDARD_INSTRUCTIONS or upper in STANDARD_GATES:
            expression[0] = upper
            if upper == 'MEASURE':
                yield replace_defs('{} {} [{}]'.format(*expression))
            else:
                yield replace_defs(' '.join(expression))
        elif head == 'def':
            assert len(expression) in [3, 4, 5], 'Def expressions should take the form (def var val) or (def var start end) or (def var start end type)'
            update_definitions(expression, definitions)
        elif hasattr(constructs, head):
            module  = getattr(constructs, head)
            creator = getattr(module, 'create_' + head)
            yield replace_defs(creator(*expression[1:], definitions=definitions))
        else:
            print('No generation branch for:')
            print(head)
            print('In:')
            print(expression)
            sys.exit(1)

def generate_single(expression):
    return generate([expression])

def generate(stack):
    pprint(stack)
    l = list(build(stack))
    return '\n'.join(l)
