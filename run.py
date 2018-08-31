#!/usr/bin/env python3
import sys

from pyquil.quil  import Program
from pyquil.api   import QVMConnection

from math import floor, log

bitstr  = lambda n : str(bin(n))[2:]

def run(filename):
    with open(filename, 'r') as infile:
        quil = infile.read()
    program = Program(quil)
    qvm = QVMConnection()
    wave_function = qvm.wavefunction(program)
    print(wave_function)
    print(wave_function.pretty_print_probabilities())
    probs = wave_function.pretty_print_probabilities()
    rbitstr = lambda n : bitstr(n)[::-1].ljust(floor(log(len(probs), 2)), '0')
    #lprobs = [probs[rbitstr(i)] for i in range(len(probs))]
    #print('Retrieved probabilities:')
    #print(lprobs)
    print(probs)

def main(args):
    assert len(args) > 0, 'Usage: ./run [filename]'
    filename = args[0]
    run(filename)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
