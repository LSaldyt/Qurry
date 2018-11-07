from ..multinomial import multinomial

def create_multinomial(*args, definitions):
    '''
    Create a discrete multinomial distribution across several qubits
    (multinomial 0.1 0.1 0.8 blockb) # Use two qubits to create the multinomial
    '''
    weights = [float(x) for x in args[:-1]]
    return multinomial(*weights, offset=args[-1], definitions=definitions)
