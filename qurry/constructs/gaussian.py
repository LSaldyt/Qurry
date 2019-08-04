from math import erf, sqrt
from functools import partial

from ..library.multinomial import multinomial, to_multinomial

def gaussian_cdf(x, mu, sigma):
    y = (1.0 + erf((x - mu) / (sigma * sqrt(2.0)))) / 2.0
    y = (1.0 + erf((x) / (sqrt(2.0)))) / 2.0
    assert y >= 0 and y <= 1.0, 'y is not a valid probability: y={}'.format(y)
    return y

def gaussian_cdfp(mu, sigma):
    return partial(gaussian_cdf, mu=mu, sigma=sigma)

def gaussian(mu, sigma, block, kernel=None):
    '''
    Construct to create a discrete approximation of the gaussian distribution using mu and sigma
    (gaussian 0 1 blocka)
    '''
    return multinomial(*multinomial(-3, 3, 64, gaussian_cdfp(float(mu), float(sigma))), offset=block, definitions=kernel.definitions)

