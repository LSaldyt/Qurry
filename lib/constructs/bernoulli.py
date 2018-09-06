from ..controlled import bernoulli as bernoulli_inner

def create_bernoulli(p, q, rot='RX', definitions=None):
    if definitions is None:
        definitions = dict()
    p = float(p)
    yield bernoulli(p, q, rot=rot)
