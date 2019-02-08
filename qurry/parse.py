'''
Parse curry (lisp) code.
'''

def remove_comment(line):
    if ';' not in line:
        return line
    else:
        return line[:line.find(';')]

def typify(item):
    '''
    Error-free conversion of an abitrary AST element into typed versions
    i.e. ['X', '1'] becomes ['X', 1] where the second element is converted str->int
    '''
    try:
        return int(item)
    except ValueError:
        try:
            return float(item)
        except ValueError:
            return item
    except TypeError:
        return [typify(subitem) for subitem in item]

def parse(item):
    '''
    item is the raw text of a q-lisp file
    Comments are removed, and then the parentheses are parsed, i.e.
          (if (= c0 1) (X 0) (X 1))
      becomes the python list:
          ['if', ['=', 'c0', '1'], ['X', '0'], ['X', '1']]
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
