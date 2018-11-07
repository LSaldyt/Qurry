from ..utils import named_uuid

clear_template = '''# Clearing qubit {q}
MEASURE {q} [{scratch_bit}]
JUMP-UNLESS @{uuid} [{scratch_bit}]
X {q}
LABEL @{uuid}'''

def create_clear(q, scratch=63, definitions=None):
    '''
    Clear the qubit q and reset it to the 0 state
    (clear 0)
    '''
    if definitions is None:
        definitions = dict()
    return clear_template.format(q=q, scratch_bit=scratch, uuid=named_uuid('qubit-{}'.format(q)))
