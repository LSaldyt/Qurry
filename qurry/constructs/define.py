from ..definitions import update_definitions

def define(*expression, definitions=None, builder=None):
    name, *rest = expression
    definitions[name] = rest
    return ''
