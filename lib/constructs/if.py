from ..utils import named_uuid

if_template = '''# Conditional statement
JUMP-WHEN @{first} [{cond}]
  {b}
JUMP @{end}
LABEL @{first}
  {a}
LABEL @{end}'''

def create_if(cond, a, b, definitions=None):
    '''
    Create an if statement using labels and jumps.
    (if (equal 0 1) (X 1) (X 0))
    '''
    if definitions is None:
        definitions = dict()
    return if_template.format(
            cond=cond,
            a=a,
            b=b,
            first=named_uuid('first'),
            end=named_uuid('end'))
