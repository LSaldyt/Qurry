#!/usr/bin/env python3
import sys, time

import seaborn
import matplotlib.pyplot as plt
from math import floor, log

from pyquil import get_qc
from pyquil.latex import to_latex
from pyquil.quil  import Program
from pyquil.api   import QVMConnection

bitstr  = lambda n : str(bin(n))[2:]

'''
This script runs a .quil file using an active quilc and qvm server.
The servers can be started by running the `server` script: `./server &`
'''

def run(filename):
    with open(filename, 'r') as infile:
        quil = infile.read()
    program = Program(quil)
    with open('test.tex', 'w') as outfile:
        outfile.write(to_latex(program))
    qvm = get_qc('9q-square-qvm')
    result = qvm.run(program)
    print(result)

def main(args):
    assert len(args) > 0, 'Usage: ./run [filename]'
    filename = args[0]
    run(filename)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
