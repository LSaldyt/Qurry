from ..utils import named_uuid

do_template = '''# Do block
{}
'''

def create_do(*l, definitions=None):
    '''
    Simply create a chain of operations. Useful inside of if statements
    (do (X 0) (X 1))
    '''
    if definitions is None:
        definitions = dict()
    return do_template.format('\n'.join(l))
