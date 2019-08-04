from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES
import pyquil as _pyquil
from pyquil.gates import *
from pyquil import Program

from functools import wraps

from .constructs import CONSTRUCTS

# Genuinely not sure what this does, or what it was planned for
# def pyquilify(f):
#     @wraps(f)
#     def f(*args, **kwargs):
#         return f(*args, **kwargs)
#     return f

for k, v in CONSTRUCTS.items():
    vars()[k] = getattr(v, k)
