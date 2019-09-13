#!/usr/bin/env python3
import inspect

def curry(creator, *args, kernel=None):
    aspec = inspect.getfullargspec(creator)
    arguments = aspec.args[:-1]
    if len(arguments) == len(args):
        return creator(*args, kernel=kernel)
    else:
        print(arguments)
        print(args)
        # TODO Wrap
        def curried_function(*remaining):
            return creator(*args, *remaining, kernel=kernel)
        return curried_function
