import sys

from pprint import pprint

from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES
import pyquil

from .utils import named_uuid
from .definitions import update_definitions

from . import constructs

from math import acos, asin, sin, cos, sqrt

'''
This file contains the "meat and potatoes" of the curry.
'''

def replace_defs(code, definitions):
    for item, block in definitions.items():
        code = code.replace(item, block.expand())
    return code

def build_expression(expression, definitions=None):
    '''
    Recursively build sub-expressions in larger expression
    '''
    if definitions is None:
        definitions = dict()
    expression = ['\n'.join(build([item], definitions)) if isinstance(item, list) else item for item in expression]
    # Break the expression into parts
    head = expression[0]
    upper = head.upper()
    # Use instructions from the QUIL spec
    if upper in STANDARD_INSTRUCTIONS or upper in STANDARD_GATES:
        expression[0] = upper
        if upper == 'MEASURE':
            return replace_defs('{} {} [{}]'.format(*expression), definitions)
        else:
            return replace_defs(' '.join(expression), definitions)
    # Custom branch for def instructions
    elif head == 'def':
        assert len(expression) in [3, 4, 5], 'Def expressions should take the form (def var val) or (def var start end) or (def var start end type)'
        update_definitions(expression, definitions)
    # Branch for language constructs defined in the `constructs` directory
    elif hasattr(constructs, head):
        module  = getattr(constructs, head)
        creator = getattr(module, head)
        return replace_defs(creator(*expression[1:], definitions=definitions), definitions)
    else:
        print('No generation branch for: {}'.format(expression))
        sys.exit(1)

def build_python_expression(expression, definitions=None):
    return pyquil.Program(build_expression(expression, definitions))

def build(stack, definitions=None):
    '''
    Create quil code from a curry abstract syntax tree
    '''
    if definitions is None:
        definitions = dict()

    for expression in stack:
        assert len(expression) > 0, 'Error: parsed empty list {}'.format(expression)
        yield build_expression(expression, definitions)

# Helper function for debugging a single expression
def generate_single(expression):
    return generate([expression])

# Full function to generate code (quil string) from AST
def generate(stack):
    pprint(stack)
    l = list(build(stack))
    return '\n'.join(l)

def generate_program(stack):
    return pyquil.Program(generate(stack))
