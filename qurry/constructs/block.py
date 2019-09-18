from ..datatypes.block import Block

def block(*rest, kernel=None):
    first = rest[0]
    rest  = rest[1:]
    defined = Block(0, int(first) + 1, *rest)
    _, defined = kernel.memory.allocate(defined)
    return defined

