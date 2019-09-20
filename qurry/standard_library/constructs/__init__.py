from os.path import dirname, basename, isfile
import glob
import importlib

modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

# CONSTRUCTS = [importlib.import_module('.' + basename(f)[:-3], package=__name__)
#               for f in modules if isfile(f) and not f.endswith('__init__.py')]
CONSTRUCTS = {basename(f)[:-3] : importlib.import_module('.' + basename(f)[:-3], package=__name__)
              for f in modules if isfile(f) and not f.endswith('__init__.py')}

#print(CONSTRUCTS)
