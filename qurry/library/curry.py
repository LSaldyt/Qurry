#!/usr/bin/env python3
from functools import wraps

import inspect

class CurriedFunction:
    def __init__(self, f):
        self.f = f
        self.__name__ = f.__name__

    def __call__(self, *args, kernel=None):
        return self.f(*args, kernel=kernel)

    def __str__(self):
        return ''

def curry(creator, *args, kernel=None):
    aspec = inspect.getfullargspec(creator)
    arguments = aspec.args[:-1]
    if len(arguments) <= len(args):
        return creator(*args, kernel=kernel)
    else:
        @wraps(creator)
        def curried_function(*remaining, kernel=kernel):
            return creator(*args, *remaining, kernel=kernel)
        return CurriedFunction(curried_function)
