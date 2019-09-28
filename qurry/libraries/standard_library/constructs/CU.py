def CU(unitary, unitary_block, control, kernel=None):
    return ['CONTROLLED', unitary, unitary_block, control]
