from pyquil.gates import ALL_GATES

from pprint import pprint

from .templates import if_template
from .utils     import named_uuid

def create_if(cond, a, b):
    return if_template.format(
            cond=cond,
            a=generate_single(a),
            b=generate_single(b),
            first=named_uuid('first'),
            end=named_uuid('end'))

def build(stack):
    for expression in stack:
        assert len(expression) > 0, 'Error: parsed empty list {}'.format(item)
        head = expression[0]
        if head in ALL_GATES:
            if head == 'MEASURE':
                yield '{} {} [{}]'.format(*expression)
            else:
                yield ' '.join(expression)
        elif head == 'if':
            yield create_if(*expression[1:])
        else:
            print(head)
            1/0

def generate_single(expression):
    return generate([expression])

def generate(stack):
    pprint(stack)
    return '\n'.join(build(stack))
