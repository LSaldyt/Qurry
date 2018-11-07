from ..multinomial import multinomial

def create_uniform(*args, definitions):
    '''
    Discrete uniform distribution. Special case of multinomial.
    (uniform blocka)
    '''
    try:
        n      = int(args[0])
    except TypeError:
        raise TypeError('(uniform n) expects an integer argument')
    offset = args[1]
    return multinomial(*(1/n for _ in range(n)), offset=offset, definitions=definitions)
