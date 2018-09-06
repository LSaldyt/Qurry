from ..multinomial import multinomial as multinomial_inner

def create_multinomial(*args, definitions):
    return multinomial_inner(*args, definitions)
