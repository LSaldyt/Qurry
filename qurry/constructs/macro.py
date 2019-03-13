from ..utils import named_uuid

macro_template = '''
{body}
'''

def macro(name, arguments, *body, definitions=None, builder=None):
    end_id = named_uuid(name + '-end')
    f_id   = named_uuid(name)

    return ''
