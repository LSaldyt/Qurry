from ..library.curry import curry, CurriedFunction

from .la import la
from functools import reduce

def extract_arguments(body):
    if isinstance(body, list):
        return reduce(set.union, (extract_arguments(b) for b in body))
    elif isinstance(body, str) and '%' in body:
        return {body.split('%')[1]}
    else:
        return set()

def l(outer_body, kernel=None):
    arguments = ['%' + arg for arg in extract_arguments(outer_body)]
    return la(arguments, outer_body)
