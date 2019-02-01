from pyquil.api import get_qc
from pyquil.quil import Program


def setup_forest_objects():
    qc = get_qc("9q-square-qvm")
    return qc


def build_wf_ansatz_prep():
    program = Program("""
# set up memory
DECLARE ro BIT[4]
DECLARE theta REAL

# set up initial state
X 0
X 1

# build the exponentiated operator
RX(pi/2) 0
H 1
H 2
H 3

CNOT 0 1
CNOT 1 2
CNOT 2 3
RZ(theta) 3
CNOT 2 3
CNOT 1 2
CNOT 0 1

RX(-pi/2) 0
H 1
H 2
H 3

# measure out the results
MEASURE 0 ro[0]
MEASURE 1 ro[1]
MEASURE 2 ro[2]
MEASURE 3 ro[3]""")
    return program


# some constants
bond_step, bond_min, bond_max = 0.05, 0, 200
angle_step, angle_min, angle_max = 0.1, 0, 63
convolution_coefficients = [0.1698845197777728, 0.16988451977777283, -0.2188630663199042,
                            -0.2188630663199042]
shots = 1000

# set up the Forest object
qc = setup_forest_objects()

# set up the Program object, ONLY ONCE
program = build_wf_ansatz_prep().wrap_in_numshots_loop(shots=shots)
binary = qc.compile(program)

# get all the unweighted expectations for all the sample wavefunctions
occupations = list(range(angle_min, angle_max))
indices = list(range(4))
for offset in occupations:
    bitstrings = qc.run(binary, {'theta': [angle_min + offset * angle_step]})

    totals = [0, 0, 0, 0]
    for bitstring in bitstrings:
        for index in indices:
            totals[index] += bitstring[index]
    occupations[offset] = [t / shots for t in totals]

# compute minimum energy as a function of bond length
min_energies = list(range(bond_min, bond_max))
for bond_length in min_energies:
    energies = []
    for offset in range(angle_min, angle_max):
        energy = 0
        for j in range(4):
            energy += occupations[offset][j] * convolution_coefficients[j]
        energies.append(energy)

    min_energies[bond_length] = min(energies)

min_index = min_energies.index(min(min_energies))
min_energy, relaxed_length = min_energies[min_index], min_index * bond_step
print(min_energy)
