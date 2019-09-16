from ..library.curry import curry, CurriedFunction

def l(argnames, body, kernel=None):
    def lambda_function(*argvalues):
        if len(argvalues) == len(argnames):
            body = [kernel.builder(element) for element in body]
        else:
            body = []
    return CurriedFunction(lambda_function)
