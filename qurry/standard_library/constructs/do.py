from ..compiler.utils import named_uuid

do_template = '''# Do block
{}
'''

def do(*l, kernel=None):
    '''
    Simply create a chain of operations. Useful inside of if statements
    (do (X 0) (X 1))
    '''
    return do_template.format('\n'.join(l))
