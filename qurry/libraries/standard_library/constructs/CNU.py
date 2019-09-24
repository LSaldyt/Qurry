from .CU import CU

def CNU(control_qubits, work_qubits, unitary, unitary_block, kernel=None):
    '''
    The fabled Controlled-N Unitary Operator!
    '''
    control_qubits = kernel.definitions[control_qubits]
    work_qubits    = kernel.definitions[work_qubits]
    print(control_qubits)
    print(work_qubits)
    print(work_qubits.end - work_qubits.start)
    print(control_qubits.end - control_qubits.start)
    assert (work_qubits.end - work_qubits.start) == (control_qubits.end - control_qubits.start) - 1, 'CNU Requires N-1 work qubits for N control qubits'
    code = []
    for i in range(control_qubits.start, control_qubits.end - 1):
        j = work_qubits.start + i
        code.append(['CNOT', i, j])
    code.append(CU(unitary, unitary_block, work_qubits.end - 1, kernel=kernel))
    return code
