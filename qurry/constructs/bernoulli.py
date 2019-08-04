from ..library.controlled import bernoulli as _bern

def bernoulli(p, q, rot='RX', kernel=None):
    '''
    Exploit an RX gate to create a simple bernoulli trial
    (bernoulli 0.5 0) # Create the 0.5 state on qubit 0
    '''
    p = float(p)
    return _bern(p, q, rot=rot)
