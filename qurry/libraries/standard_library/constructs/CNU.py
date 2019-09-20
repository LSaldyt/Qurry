from .CU import CU

def CNU(control_qubits, work_qubits, unitary, unitary_block, kernel=None):
    '''
    The fabled Controlled-N Unitary Operator!
    '''
    control_qubits = kernel.definitions[control_qubits]
    work_qubits    = kernel.definitions[work_qubits]
    assert (work_qubits.end - work_qubits.start) == (control_qubits.end - control_qubits.start) - 1, 'CNU Requires N-1 work qubits for N control qubits'
    code = ''
    for i in range(control_qubits.start, control_qubits.end - 1):
        j = work_qubits.start + i
        code += 'CNOT {} {}\n'.format(i, j)
    code += CU(unitary, unitary_block, work_qubits.end - 1, kernel=kernel)
    return code
