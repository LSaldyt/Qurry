from math import erf, sqrt
from functools import partial

from ..multinomial import multinomial
from ..to_multinomial import to_multinomial

def gaussian_cdf(x, mu, sigma):
    y = (1.0 + erf((x - mu) / (sigma * sqrt(2.0)))) / 2.0
    y = (1.0 + erf((x) / (sqrt(2.0)))) / 2.0
    assert y >= 0 and y <= 1.0, 'y is not a valid probability: y={}'.format(y)
    return y

def create_gaussian_cdf(mu, sigma):
    return partial(gaussian_cdf, mu=mu, sigma=sigma)

def create_gaussian(mu, sigma, block, definitions=None):
    return multinomial(*to_multinomial(-3, 3, 64, create_gaussian_cdf(float(mu), float(sigma))), offset=block, definitions=definitions)

