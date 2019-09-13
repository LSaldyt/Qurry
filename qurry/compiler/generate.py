import sys

from pprint import pprint

from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES
import pyquil

from .utils import named_uuid
from ..datatypes import update_definitions
from ..datatypes import Datatype
from ..kernel import Kernel
from ..library.curry import curry

from .. import constructs

from math import acos, asin, sin, cos, sqrt

'''
This file contains the "meat and potatoes" of Qurry.
'''

def lookup(expr, definitions):
    root, *terms = expr.split('.')
    assert root in definitions, '{} is not defined properly'.format(root)
    root = definitions[root]
    for term in terms:
        if hasattr(root, 'fields') and term in root.fields:
            root = root.fields[term]
        else:
            root = root.mapping[term]
    return root

def expand_property(word, definitions):
    if isinstance(word, list):
        return [expand_property(subword, definitions) for subword in word]
    elif '.' in word:
        return lookup(word, definitions).expand()
    else:
        return word

def build_expression(expression, kernel):
    '''
    Recursively build sub-expressions in larger expression
    '''
    expression = [expand_property(item, kernel.definitions) for item in expression]

    # Break the expression into parts
    head = expression[0]
    upper = head.upper()
    # Use instructions from the QUIL spec
    if upper in STANDARD_INSTRUCTIONS or upper in STANDARD_GATES or upper in {'DAGGER', 'CONTROLLED'}:
        expression[0] = upper
        if upper == 'MEASURE':
            return '{} {} [{}]'.format(*expression)
        else:
            return ' '.join(expression)
    # Branch for language constructs defined in the `constructs` directory
    elif hasattr(constructs, head):
        module  = getattr(constructs, head)
        creator = getattr(module, head)
        #curry(creator, *expression[1:], kernel=kernel)
        return creator(*expression[1:], kernel=kernel)
    else:
        print('No generation branch for: {}'.format(expression))
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
    pprint(dir(constructs))
    intermediate = generate(stack, kernel)
    print(intermediate)
    return pyquil.Program(intermediate)
