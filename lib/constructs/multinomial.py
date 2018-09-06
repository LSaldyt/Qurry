from ..multinomial import multinomial as multinomial_inner

def create_multinomial(*args, definitions):
    weights = [float(x) for x in args[:-1]]
    return multinomial_inner(*weights, offset=args[-1], definitions=definitions)
