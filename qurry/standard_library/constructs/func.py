from .l  import l

def func(name, body, kernel=None):
    f = l(body, kernel=kernel)
    kernel.define(name, f)
    return f
