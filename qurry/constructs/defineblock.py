from ..datatypes import update_definitions

def defineblock(*expression, definitions=None, builder=None):
    assert len(expression) in [2, 3, 4], 'Def expressions should take the form (def var val) or (def var start end) or (def var start end type)'
    update_definitions(expression, definitions)
    return ''
