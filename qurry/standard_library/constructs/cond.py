from ..compiler.utils import named_uuid

if_template = '''# Conditional statement
JUMP-WHEN @{first} [{cond}]
  {b}
JUMP @{end}
LABEL @{first}
  {a}
LABEL @{end}'''

def cond(cond, a, b, kernel=None):
    '''
    Create an if statement using labels and jumps.
    (cond 0 (X 1) (X 0))
    if qubit 0 == 1:
        X 1
    else:
        X 0
    '''
    if definitions is None:
        definitions = dict()
    return if_template.format(
            cond=cond,
            a=a,
            b=b,
            first=named_uuid('first'),
            end=named_uuid('end'))
