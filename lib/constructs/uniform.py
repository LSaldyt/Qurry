from ..multinomial import multinomial

def create_uniform(*args, definitions):
    try:
        n      = int(args[0])
        offset = int(args[1])
    except TypeError:
        raise TypeError('(uniform n) expects an integer argument')
    return multinomial(*(1/n for _ in range(n)), offset=offset, definitions=definitions)
