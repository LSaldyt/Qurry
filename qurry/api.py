#!/usr/bin/env python3

import sys
from pyquil import get_qc

from .compiler.parse    import parse
from .compiler.generate import generate_program, build_expression
from .kernel            import Kernel, Topology
from .postprocess       import postprocess

def run(filename, computer='9q-square-qvm', topology=None, indir='examples', outdir='examples/quil/', diagramdir='examples/diagrams', trials=10, postprocess=False):

    if topology is None:
        topology = Topology(36, None)

    with open(indir + '/' + filename + '.lisp', 'r') as infile:
        body = infile.read()

    stack   = parse(body)
    kernel  = Kernel(build_expression, topology, ['standard_library', 'test_library'])
    circuit, program = generate_program(stack, kernel)

    print('Program:')
    print(program)
    print('End')

    quil = str(program)
    with open(outdir + '/' + filename + '.quil', 'w') as outfile:
        outfile.write(quil)
    with open(diagramdir + '/' + filename + '.qpic', 'w') as outfile:
        outfile.write(circuit)

    # Commented out temp
    # qc = get_qc(computer)
    # result = qc.run_and_measure(program, trials=trials)
    # if postprocess:
    #     postprocess(result)
