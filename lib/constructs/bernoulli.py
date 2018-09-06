from ..controlled import bernoulli

def create_bernoulli(p, q, rot='RX', definitions=None):
    if definitions is None:
        definitions = dict()
    p = float(p)
    return bernoulli(p, q, rot=rot)
