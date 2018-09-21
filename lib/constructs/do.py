from ..utils import named_uuid

do_template = '''# Do block
{}
'''

def create_do(*l, definitions=None):
    if definitions is None:
        definitions = dict()
    return do_template.format('\n'.join(l))
