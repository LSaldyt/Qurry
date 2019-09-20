def CU(unitary, unitary_block, control, kernel=None):
    return 'CONTROLLED {} {} {}'.format(unitary, unitary_block, control)
