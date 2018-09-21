#!/usr/bin/env python3
import sys, time
from math import erf, sqrt

def phi_normal(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def to_multinomial(a, b, n, phi):
    assert n >= 3, 'Minimum three discrete divisions required'
    n -= 2
    step  = (b - a) / n
    return discrete_multinomial_probabilities(a, b, step, phi)

def discrete_multinomial_probabilities(a, b, step, phi):
    probabilities = []
    i = a
    while i < b:
        probabilities.append(phi(i) - sum(probabilities))
        i += step
    probabilities.append(phi(b) - sum(probabilities))
    probabilities.append(phi(float('inf')) - sum(probabilities))
    return probabilities

def main(args):
    start = time.time()
    print(to_multinomial(-3, 3, 100, phi_normal))
    end = time.time()
    print(round((end - start) * 1000, 3), 'ms')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
