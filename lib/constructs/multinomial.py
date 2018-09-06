from ..multinomial import multinomial

def create_multinomial(*args, definitions):
    weights = [float(x) for x in args[:-1]]
    return multinomial(*weights, offset=args[-1], definitions=definitions)
