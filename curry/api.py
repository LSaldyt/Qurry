from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES
import pyquil as _pyquil
from pyquil.gates import *

from pyquil import Program

from .constructs import CONSTRUCTS
#from . import constructs as _constructs

from functools import wraps

def pyquilify(f):
    @wraps(f)
    def f(*args, **kwargs):
        return f(*args, **kwargs)
    return f

#print(constructs)
#for item in dir(_constructs):
#    if '__' not in item:
#        f = getattr(getattr(_constructs, item), item)
#        __dict__[item] = pyquilify(f)
#print(CONSTRUCTS)
for k, v in CONSTRUCTS.items():
    vars()[k] = getattr(v, k)
