import sys

from pprint import pprint

from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES
import pyquil

from .utils import named_uuid
from .definitions import update_definitions
from .datatype import Datatype
from .kernel import Kernel

from . import constructs

from math import acos, asin, sin, cos, sqrt

'''
This file contains the "meat and potatoes" of the curry.
'''

def replace_defs(code, definitions):
    for item, block in definitions.items():
        if hasattr(block, 'expand'):
            code = code.replace(item, block.expand())
    return code

def expand_property(word):
    if isinstance(word, list):
        return [expand_property(subword) for subword in word]
    else:
        return word # TODO

def build_expression(expression, kernel):
    '''
    Recursively build sub-expressions in larger expression
    '''
    expression = [expand_property(item) for item in expression]

    # Break the expression into parts
    head = expression[0]
    upper = head.upper()
    # Use instructions from the QUIL spec
    if upper in STANDARD_INSTRUCTIONS or upper in STANDARD_GATES:
        expression[0] = upper
        if upper == 'MEASURE':
            return replace_defs('{} {} [{}]'.format(*expression), kernel.definitions)
        else:
            return replace_defs(' '.join(expression), kernel.definitions)
    # Branch for language constructs defined in the `constructs` directory
    elif hasattr(constructs, head):
        module  = getattr(constructs, head)
        creator = getattr(module, head)
        return replace_defs(creator(*expression[1:], kernel=kernel), kernel.definitions)
    else:
        print('No generation branch for: {}'.format(expression))
        pprint(definitions)
        sys.exit(1)

def build_python_expression(expression, kernel):
    return pyquil.Program(build_expression(expression, definitions))

def build(stack, kernel):
    '''
    Create quil code from a curry abstract syntax tree
    '''
    for expression in stack:
        assert len(expression) > 0, 'Error: parsed empty list {}'.format(expression)
        yield build_expression(expression, kernel)

# Helper function for debugging a single expression
def generate_single(expression, definitions=None):
    return generate([expression], definitions)

# Full function to generate code (quil string) from AST
def generate(stack, kernel):
    pprint(stack)
    l = list(build(stack, kernel))
    return '\n'.join(l)

def generate_program(stack, kernel):
    return pyquil.Program(generate(stack, kernel))
