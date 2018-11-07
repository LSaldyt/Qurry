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

def run(filename):
    with open(filename, 'r') as infile:
        quil = infile.read()
    program = Program(quil)
    with open('test.tex', 'w') as outfile:
        outfile.write(to_latex(program))
    qvm = get_qc('9q-square-qvm')
    result = qvm.run(program)
    print(result)
    #qvm = QVMConnection()
    #start = time.time()
    #result = qvm.run_and_measure(p, trials=10)
    #print(result)
    #wave_function = qvm.wavefunction(program)
    #print(wave_function)
    #print(wave_function.pretty_print_probabilities())
    #probs = wave_function.pretty_print_probabilities()
    #rbitstr = lambda n : bitstr(n)[::-1].ljust(floor(log(len(probs), 2)), '0')
    ##lprobs = [probs[rbitstr(i)] for i in range(len(probs))]
    ##print('Retrieved probabilities:')
    ##print(lprobs)
    #print(probs)
    #end = time.time()
    #print((end-start) * 1000, 'ms simulated runtime')
    #probs_ordered = [t[1] for t in sorted(probs.items(), key=lambda t : int(t[0][::-1], 2))]
    #print(probs_ordered)
    #seaborn.set()
    #seaborn.scatterplot(x=list(range(len(probs_ordered))), y=probs_ordered)
    #plt.show()

def main(args):
    assert len(args) > 0, 'Usage: ./run [filename]'
    filename = args[0]
    run(filename)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
