import sys

from pprint import pprint

from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES
import pyquil

#from ..standard_library import constructs
from ..libraries.standard_library.library.curry import curry

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
        return expression
        #if upper == 'MEASURE':
        #    #return '{} {} [{}]'.format(*expression)
        #else:
        #    return expression
        #    #return ' '.join(expression)
    elif kernel.is_construct(head):
        creator = kernel.get_construct(head)
        return curry(creator, *expression[1:], kernel=kernel)
    elif head in kernel.definitions:
        return curry(kernel.definitions[head], *expression[1:], kernel=kernel)
    else:
        print('"{}"'.format(head))
        print(dir(kernel.libraries['standard_library'].constructs))
        print(kernel.is_construct(head))
        print('No generation branch for: {} (head={})'.format(expression, head))
        pprint(kernel.definitions)
        sys.exit(1)

def generate_program(stack, kernel):
    pprint(stack)
    l = [build_expression(expression, kernel) for expression in stack]
    print(l)
    1/0
    with open('.qpic.out', 'w') as outfile:
        outfile.write(generate_qpic(l, kernel))
    intermediate = '\n'.join(map(str, l))
    print(intermediate)
    return pyquil.Program(intermediate)

def generate_qpic(expanded, kernel):
    qpic = ''
    qubits = kernel.topology.size
    for i in range(qubits):
        qpic += ('a{} W |\\psi_{}\\rangle'.format(i, i)) + '\n'
    for line in expanded:
        first, *rest = line.split(' ')
        if first == 'CNOT':
            qpic += 'a{} +a{}'.format(*rest) + '\n'
        elif first == 'MEASURE':
            first = 'M'
            rest = [item.replace('[', '').replace(']', '') for item in rest]
            qpic += '{} {}'.format(' '.join(rest), first) + '\n'
        else:
            qpic += '{} {}'.format(' '.join(rest), first) + '\n'

    pprint(expanded)
    return qpic
