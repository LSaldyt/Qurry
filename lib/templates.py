if_template = '''
JUMP-WHEN @{first} [{cond}]
  {b}
JUMP @{end}
LABEL @{first}
  {a}
LABEL @{end}'''
