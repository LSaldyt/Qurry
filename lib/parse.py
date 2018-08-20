
def remove_comment(line):
    if ';' not in line:
        return line
    else:
        return line[:line.find(';')]

def parse(item):
    '''
    item is the raw text of a q-lisp file
    '''
    cleaned = (remove_comment(line) for line in item.split('\n'))
    item = '\n'.join(line for line in cleaned if line != '') # Strip comments
    stack = []
    depth = 0
    inner = ''
    def add(item):
        current = stack
        for _ in range(depth):
            current = current[-1]
        if isinstance(item, str):
            for subitem in item.split():
                current.append(subitem)
        else:
            current.append(item)
    for character in item.strip():
        if character == '(':
            if inner.strip() != '':
                add(inner.strip())
                inner = ''
            add([])
            depth += 1
        elif character == ')':
            add(inner.strip())
            depth -= 1
            inner = ''
        else:
            inner += character
    return stack
