from .block import Block

def update_definitions(expression, definitions):
    var = expression[1]
    if len(expression) == 3:
        val = expression[2]
        definitions[var] = Block(val, val)
    else:
        blocktype = expression[-1] if len(expression) == 5 else 'quantum'
        start, end = expression[2:4]
        definitions[var] = Block(start, end, blocktype)
