from ..utils import named_uuid

def defcircuit(name, argdef, expressions, definitions=None, builder=None):
    '''
    Create a repeatable circuit
    '''
    definitions['a'] = 0
    definitions['b'] = 1
    #s = generate(..)
    del definitions['a']
    del definitions['b']
    return ''
