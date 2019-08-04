#!/usr/bin/env python3

import sys
from pyquil import get_qc

from .compiler.parse    import parse
from .compiler.generate import generate, generate_program, build_expression
from .kernel            import Kernel, Topology

from pprint import pprint

def run(filename, computer='9q-square-qvm', topology=None, indir='examples', outdir='examples/quil/', trials=10):

    if topology is None:
        topology = Topology(64, None)

    with open(indir + '/' + filename + '.lisp', 'r') as infile:
        body = infile.read()

    stack   = parse(body)
    kernel  = Kernel(build_expression, topology)
    program = generate_program(stack, kernel)

    print('Program:')
    print(program)
    print('End')

    qc = get_qc(computer)
    result = qc.run_and_measure(program, trials=trials)
    pprint(result)

    quil = str(program)
    with open(outdir + '/' + filename + '.quil', 'w') as outfile:
        outfile.write(quil)
