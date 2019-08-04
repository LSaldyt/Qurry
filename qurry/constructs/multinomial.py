from ..library.multinomial import multinomial as lib_multinomial

def multinomial(*args, kernel=None):
    '''
    Create a discrete multinomial distribution across several qubits
    (multinomial 0.1 0.1 0.8 blockb) # Use two qubits to create the multinomial
    '''
    weights = [float(x) for x in args[:-1]]
    return lib_multinomial(*weights, offset=args[-1], definitions=kernel.definitions)
