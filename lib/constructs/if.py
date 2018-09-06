if_template = '''# Conditional statement
JUMP-WHEN @{first} [{cond}]
  {b}
JUMP @{end}
LABEL @{first}
  {a}
LABEL @{end}'''

def create_if(cond, a, b, definitions=None):
    if definitions is None:
        definitions = dict()
    return if_template.format(
            cond=cond,
            a=generate_single(a),
            b=generate_single(b),
            first=named_uuid('first'),
            end=named_uuid('end'))
