from ..library.curry import curry, CurriedFunction

def la(argnames, outer_body, kernel=None):
    def lambda_function(*argvalues, kernel=kernel):
        if len(argvalues) == len(argnames):
            for k, v in zip(argnames, argvalues):
                kernel.define(k, v)
            body = [kernel.builder(element, kernel=kernel) for element in outer_body]
            for k in argnames:
                kernel.definitions.pop(k)
            return '\n'.join(body)
        else:
            @wraps(lambda_function)
            def curried_function(*remaining, kernel=kernel):
                return lambda_function(*args, *remaining, kernel=kernel)
            return CurriedFunction(curried_function)
    return CurriedFunction(lambda_function)
