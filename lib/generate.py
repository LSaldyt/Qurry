import sys

from pprint import pprint

from pyquil.gates import STANDARD_INSTRUCTIONS

from .templates import if_template, clear_template
from .utils     import named_uuid

def create_if(cond, a, b):
    return if_template.format(
            cond=cond,
            a=generate_single(a),
            b=generate_single(b),
            first=named_uuid('first'),
            end=named_uuid('end'))

def create_clear(q, scratch=63):
    return clear_template.format(q=q, scratch_bit=scratch, uuid=named_uuid('qubit-{}'.format(q)))

from math import acos, asin, sin, cos, sqrt

def build(stack):
    definitions = dict()
    def insert_defs(items):
        for item in items:
            try:
                yield definitions[item]
            except KeyError:
                yield item
            except TypeError:
                yield item
    for expression in stack:
        assert len(expression) > 0, 'Error: parsed empty list {}'.format(item)
        head = expression[0]
        upper = head.upper()
        if upper in STANDARD_INSTRUCTIONS:
            expression[0] = upper
            if upper == 'MEASURE':
                yield '{} {} [{}]'.format(*insert_defs(expression))
            else:
                yield ' '.join(insert_defs(expression))
        elif head == 'if':
            yield create_if(*(insert_defs(expression[1:])))
        elif head == 'def':
            assert len(expression) == 3, 'Def expressions should take the form (def var val)'
            definitions[expression[1]] = expression[2]
        elif head == 'clear':
            assert len(expression) == 2, 'Clear expressions should look like: (clear q)'
            yield create_clear(expression[1])
        elif head == 'bernoulli':
            assert len(expression) == 3
            _, p, q = expression
            p = float(p)
            theta = 2 * acos(sqrt(p))
            yield 'RX({theta}) {q}'.format(theta=theta, q=q)
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
    return '\n'.join(build(stack))
