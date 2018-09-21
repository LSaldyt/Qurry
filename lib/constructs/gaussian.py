from math import erf, sqrt

from ..multinomial import multinomial
from ..to_multinomial import to_multinomial

def phi_normal(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def create_gaussian(mu, sigma, block, definitions=None):
    return multinomial(*to_multinomial(-3, 3, 6, phi_normal), offset=block, definitions=definitions)

