from .block import Block

'''
Add definitions (define ..) to a global dictionary.
'''
def update_definitions(args, definitions):
    var = args[0]
    if len(args) == 2:
        val = args[1]
        definitions[var] = Block(int(val), int(val))
    else:
        blocktype = args[-1] if len(args) == 4 else 'quantum'
        start, end = args[1:3]
        definitions[var] = Block(int(start), int(end), blocktype)
