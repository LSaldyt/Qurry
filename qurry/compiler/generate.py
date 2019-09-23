import sys

from pprint import pprint
from ..libraries.standard_library.library.curry import curry

from ..backends import QuilBackend, QpicBackend

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
    quil = QuilBackend()
    expression = [expand_property(item, kernel.definitions) for item in expression]

    # Break the expression into parts
    head = expression[0]
    upper = head.upper()
    # Use instructions from the QUIL spec
    if upper in quil.spec:
        expression[0] = upper
        return expression
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
    qpic = QpicBackend()
    quil = QuilBackend()

    print(qpic.generate(l, kernel=kernel))
    return quil.generate(l, kernel=kernel)
