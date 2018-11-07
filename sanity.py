from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import *
qvm = QVMConnection()
p = Program()
p.inst(H(0),
       CNOT(0, 1),
       MEASURE(0, 0),
       MEASURE(1, 1))
#qvm.run(p, [0, 1], 10)
qvm.run(p)
