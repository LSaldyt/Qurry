import pyquil
from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES

from .backend import Backend

class QuilBackend(Backend):
    def __init__(self):
        self.spec = set()
        self.spec = self.spec.union(STANDARD_INSTRUCTIONS.keys())
        self.spec = self.spec.union(STANDARD_GATES.keys())
        self.spec = self.spec.union({'DAGGER', 'CONTROLLED'})

    def generate(self, l, kernel=None):
        intermediate = '\n'.join(map(lambda x : ' '.join(map(str,x)), l))
        return pyquil.Program(intermediate)

