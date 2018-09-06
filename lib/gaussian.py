# Originally written by M. Sohaib Alam, github: msohaibalam
# Essentially unmodified and now used by LSaldyt

import numpy as np
import itertools
from pyquil.quil import Program
import pyquil.api as api

class Gaussian:

    def __init__(self, sigma_, mu_, num_qubits=5):
        """
        Specify the standard deviation and mean of the single-variable Gaussian wavefunction,
        aa well as the number of qubits to be used in the construction
        Inputs:-
        sigma_: standard deviation
        mu_: mean
        num_qubits (optional): number of qubits to be used
        """
        self.sigma = sigma_
        self.mu = mu_
        self.num_qubits = num_qubits
        self.quantum_simulator = api.QVMConnection()
        self.prog = Program()

    def norm_(self, sigma_, mu_, N):
        """
        Normalization factor for the state. Defined in Eq (7) of paper.
        Inputs:-
        sigma_: standard deviation
        mu_: mean
        N: cutoff the for the infinite sum, i.e. sum_{i=-N}^{i=N} (...)
        """
        return np.sum(
                np.exp((-(np.arange(-N, N+1, 1) - mu_)**2) /
                        float(sigma_**2)))

    def angle_(self, sigma_, mu_, N=10**3):
        """
        The angle $\alpha$ defined in Eq (12)
        Inputs:-
        sigma_: standard deviation
        mu_: mean
        N: cutoff for the infinite sum in the norm_(..)
        """
        return np.arccos(np.sqrt(
                   self.norm_(sigma_/2., mu_/2., N) / self.norm_(sigma_, mu_, N)))

    def qubit_strings(self, n):
        """
        Return a list of n-bit strings in increasing lexicographic order
        Inputs:-
        n: recursion level
        """
        qubit_strings = []
        for q in itertools.product(['0', '1'], repeat=n):
            qubit_strings.append(''.join(q))
        return qubit_strings

    def mean_qubit_combo(self, qub, mu):
        """
        Given an n-bit string, return the corresponding mean for the rotation angle
        at recursion level n
        Inputs:-
        qub: n-bit string
        mu: mean (original)
        """
        mu_out = mu
        for bit in qub:
            mu_out = (mu_out/2.) - ((1/2.)*int(bit))
        return mu_out

    def level_means(self, mu, n):
        """
        At recursion level n, return a list of all the means used for the various rotation angles
        Inputs:-
        mu: mean (original)
        n: recursion level
        """
        list_mu_out = []
        qb_strings = self.qubit_strings(n)
        for qb in qb_strings:
            mu_out = self.mean_qubit_combo(qb, mu)
            list_mu_out.append(mu_out)
        return list_mu_out

    def level_angles(self, sigma, mu, n):
        """
        At recursion level n, return a list of all the rotation angles
        Inputs:-
        sigma: standard deviation (original)
        mu: mean (original)
        n: recursion level
        """
        sigma_out = sigma/(2.**n)
        list_mu = self.level_means(mu, n)
        # for each (sigma, mu) pair, calculate the corresponding angle
        angles_out = []
        for mu_ in list_mu:
            angles_out.append(self.angle_(sigma_out, mu_))
        return angles_out

    def rotation_block(self, alpha):
        """
        Given a rotation angle $\alpha$, return a 2x2 rotation block (numpy array)
        Inputs:-
        alpha: rotation angle
        """
        return np.array([[np.cos(alpha), -np.sin(alpha)], [np.sin(alpha), np.cos(alpha)]])

    def level_gate(self, sigma, mu, n):
        """
        Return (n+1)-qubit controlled operation as a 2^(n+1) x 2^(n+1) matrix,
        with 2^n rotation blocks along the diagonal
        Inputs:-
        sigma: standard deviation (original)
        mu: mean (original)
        n: recursion level
        """
        list_row_block = []
        list_level_angles = self.level_angles(sigma, mu, n)
        for nn, angle in enumerate(list_level_angles):
            rot_block = self.rotation_block(angle)
            row_block = np.hstack((np.zeros((2, 2*nn)), rot_block, np.zeros((2, 2*(2**(n) - nn - 1)))))
            list_row_block.append(row_block)
        level_n_gate = np.vstack(tuple(list_row_block))
        return level_n_gate

    def list_all_gates(self, sigma, mu, N):
        """
        Given sigma, mu (standard dev, mean) and the number of qubits N,
        return a list of all gates used for the controlled operations required
        to produce a Gaussian wavefunction
        Inputs:-
        sigma: standard deviation (original)
        mu: mean (original)
        N: number of qubits to be used
        """
        list_gates = []
        for n in range(N):
            list_gates.append(self.level_gate(sigma, mu, n))
        return list_gates

    def defn_all_gates(self, sigma, mu, N, prog):
        """
        Define all gates specified by N qubits, for (standard deviation, mean) given by (sigma, mu),
        into the program input which is specified by prog
        Inputs:-
        sigma: standard deviation (original)
        mu: mean (original)
        N: number of qubits to be used
        prog: Program object
        """
        list_gates_ = self.list_all_gates(sigma, mu, N)
        for i, gate in enumerate(list_gates_):
            prog.defgate("Level_" + str(i) + "_gate", gate)

    def apply_all_gates(self, sigma, mu, N, prog):
        """
        Apply all controlled rotation gates to produce the Gaussian wavefunction
        Inputs:-
        sigma: standard deviation (original)
        mu: mean (original)
        N: number of qubits to be used
        prog: Program object
        """
        list_gates_ = self.list_all_gates(sigma, mu, N)
        for i, gate in enumerate(list_gates_):
            tup_gate = ("Level_" + str(i) + "_gate",) + tuple(range(i+1))
            prog.inst(tup_gate)

    def gaussian_wavefunc(self):
        """
        Create and return the Gaussian wavefunction
        """
        # define all gates to the program
        self.defn_all_gates(self.sigma, self.mu, self.num_qubits, self.prog)
        # apply all gates to the program
        self.apply_all_gates(self.sigma, self.mu, self.num_qubits, self.prog)
        # create the gaussian wavefunction
        gaussian_wavefunc = self.quantum_simulator.wavefunction(self.prog)
        return gaussian_wavefunc
