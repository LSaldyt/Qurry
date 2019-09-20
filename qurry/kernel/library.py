from importlib import import_module

class Library:
    def __init__(self, name):
        #module = import_module('.{}'.format(name), 'qurry.libraries')
        #print(module)

        ## load constructs
        #self.constructs = module.constructs
        self.constructs = import_module('.{}.constructs'.format(name), 'qurry.libraries')
        ## load utilities
        #self.library = None
        ## load utilities
        #self.datatypes = None
        #self.name = path

    def __contains__(self, name):
        return hasattr(self.constructs, name)

    def __get__(self, name):
        return getattr(self.constructs, name)
