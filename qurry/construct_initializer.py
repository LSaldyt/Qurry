from pyquil.gates import STANDARD_INSTRUCTIONS, STANDARD_GATES
import pyquil as _pyquil
from pyquil.gates import *
from pyquil import Program

from functools import wraps

from .constructs import CONSTRUCTS

for k, v in CONSTRUCTS.items():
    vars()[k] = getattr(v, k)
