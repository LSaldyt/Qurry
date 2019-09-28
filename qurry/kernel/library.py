from importlib import import_module

class Library:
    def __init__(self, name):
        #module = import_module('.{}'.format(name), 'qurry.libraries')
        #print(module)

        ## load constructs
        #self.constructs = module.constructs

        print('Loaded ' + name)
        self.constructs = import_module('.{}.constructs'.format(name), 'qurry.libraries')
        print(dir(self.constructs))
        print(hasattr(self.constructs, 'define'))

        ## load utilities
        #self.library = None
        ## load utilities
        #self.datatypes = None
        #self.name = path

    def __contains__(self, name):
        return hasattr(self.constructs, name)

    def __getitem__(self, name):
        return getattr(getattr(self.constructs, name), name)
