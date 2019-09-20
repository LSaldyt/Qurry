from .la import la

def funca(name, args, body, kernel=None):
    f = la(args, body, kernel=kernel)
    kernel.define(name, f)
    return f
