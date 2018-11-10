#!/usr/bin/env python3
import sys, time
import subprocess

#import seaborn
#import matplotlib.pyplot as plt
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
    with open('circuit.tex', 'w') as outfile:
        outfile.write(to_latex(program))
    qvm = get_qc('9q-square-qvm')
    print('Circuit output to circuit.tex')
    try:
        result = qvm.run(program)
        print(result)
    except:
        print('Warning: Program not run due to changing pyquil API. This will be updated in a future version')
    try:
        subprocess.check_output(['pdflatex', 'circuit.tex'])
        subprocess.check_output(['rm', 'circuit.log', 'circuit.aux'])
        print('Used pdflatex to output circuit to circuit.pdf')
    except:
        print('Warning: Install pdflatex to have circuit created as pdf file')

def main(args):
    assert len(args) > 0, 'Usage: ./run [filename]'
    filename = args[0]
    run(filename)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
