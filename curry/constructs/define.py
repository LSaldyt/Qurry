from ..definitions import update_definitions

def define(*expression, definitions=None):
    assert len(expression) in [2, 3, 4], 'Def expressions should take the form (def var val) or (def var start end) or (def var start end type)'
    update_definitions(expression, definitions)
    return ''
