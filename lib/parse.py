def parse(item):
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
