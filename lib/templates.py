if_template = '''# Conditional statement
JUMP-WHEN @{first} [{cond}]
  {b}
JUMP @{end}
LABEL @{first}
  {a}
LABEL @{end}'''

clear_template = '''# Clearing qubit {q}
MEASURE {q} [{scratch_bit}]
JUMP-UNLESS @{uuid} [{scratch_bit}]
X {q}
LABEL @{uuid}'''
