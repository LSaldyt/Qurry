import sys

from pprint import pprint

from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES
import pyquil

from ..kernel import Kernel

from ..standard_library.datatypes import Datatype
from ..standard_library.library.curry import curry
from ..standard_library import constructs

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
        return curry(creator, *expression[1:], kernel=kernel)
    elif head in kernel.definitions:
        return curry(kernel.definitions[head], *expression[1:], kernel=kernel)
    else:
        print('No generation branch for: {} (head={})'.format(expression, head))
        pprint(kernel.definitions)
        sys.exit(1)

def generate_program(stack, kernel):
    pprint(stack)
    l = [build_expression(expression, kernel) for expression in stack]
    intermediate = '\n'.join(map(str, l))
    print(intermediate)
    return pyquil.Program(intermediate)
