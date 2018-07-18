import unittest
import numpy as np
from lib.gaussian import Gaussian


class TestGaussian(unittest.TestCase):

    def setUp(self):
        self.gauss = Gaussian(sigma_=(2**5)/6., mu_=2**(5-1) - 0.5)

    def test_qubit_strings_0(self):
        qub_strings = self.gauss.qubit_strings(0)
        self.assertEqual(qub_strings, [''])

    def test_qubit_strings_1(self):
        qub_strings = self.gauss.qubit_strings(1)
        self.assertEqual(qub_strings, ['0', '1'])

    def test_qubit_strings_2(self):
        qub_strings = self.gauss.qubit_strings(2)
        self.assertEqual(qub_strings, ['00', '01', '10', '11'])

    def test_qubit_strings_3(self):
        qub_strings = self.gauss.qubit_strings(3)
        self.assertEqual(qub_strings, ['000', '001', '010', '011',
                                        '100', '101', '110', '111'])

    def test_qubit_strings_4(self):
        qub_strings = self.gauss.qubit_strings(4)
        self.assertEqual(qub_strings, ['0000', '0001', '0010', '0011', '0100',
            '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
            '1101', '1110', '1111'])

    def test_mean_qubit_combo_000(self):
        mu = 1.2
        mu_out = self.gauss.mean_qubit_combo('000', mu)
        mu_expected = (((mu)/2.)/2.)/2.
        self.assertEqual(mu_out, mu_expected)

    def test_mean_qubit_combo_010(self):
        mu = 0.76
        mu_out = self.gauss.mean_qubit_combo('010', mu)
        mu_expected = (((mu/2.) - 1.)/2.)/2.
        self.assertEqual(mu_out, mu_expected)

    def test_mean_qubit_combo_10101(self):
        mu = 10.78
        mu_out = self.gauss.mean_qubit_combo('10101', mu)
        mu_expected = (((((((mu - 1.)/2.)/2.) - 1.)/2.)/2.) - 1.)/2.
        self.assertEqual(mu_out, mu_expected)

    def test_mean_qubit_combo_11111(self):
        mu = 3.02
        mu_out = self.gauss.mean_qubit_combo('11111', mu)
        mu_expected = (((((((((mu - 1.)/2.) - 1.)/2.) - 1.)/2.) - 1.)/2.) - 1.)/2.
        self.assertEqual(mu_out, mu_expected)

    def test_mean_qubit_combo_1001(self):
        mu = 19.43
        mu_out = self.gauss.mean_qubit_combo('1001', mu)
        mu_expected = (((((mu - 1.)/2.)/2.)/2.) - 1.)/2.
        self.assertEqual(mu_out, mu_expected)

    def test_mean_qubit_combo_110(self):
        mu = 27.06
        mu_out = self.gauss.mean_qubit_combo('110', mu)
        mu_expected = ((((mu - 1.)/2.)-1.)/2.)/2.
        self.assertEqual(mu_out, mu_expected)

    def test_level_gate_0_diag(self):
        sigma = 1.0
        mu = 1.0
        gate_ = self.gauss.level_gate(sigma, mu, 0)
        self.assertTrue(gate_[0][0] == gate_[1][1])

    def test_level_gate_0_anti_diag(self):
        sigma = 1.0
        mu = 1.0
        gate_ = self.gauss.level_gate(sigma, mu, 0)
        self.assertTrue(gate_[0][1] == -gate_[1][0])

    def test_level_gate_0_sincosrow0(self):
        sigma = 1.0
        mu = 1.0
        gate_ = self.gauss.level_gate(sigma, mu, 0)
        self.assertEqual((gate_[0][0])**2 + (gate_[0][1])**2, 1.)

    def test_level_gate_0_sincosrow1(self):
        sigma = 1.0
        mu = 1.0
        gate_ = self.gauss.level_gate(sigma, mu, 0)
        self.assertEqual((gate_[1][0])**2 + (gate_[1][1])**2, 1.)

    def test_level_gate_1_diag(self):
        sigma = 3.5
        mu = 5.0
        gate_ = self.gauss.level_gate(sigma, mu, 1)
        rotblock0 = (gate_[0][0] == gate_[1][1])
        rotblock1 = (gate_[2][2] == gate_[3][3])
        self.assertTrue(rotblock0 and rotblock1)

    def test_level_gate_1_anti_diag(self):
        sigma = 3.5
        mu = 5.0
        gate_ = self.gauss.level_gate(sigma, mu, 1)
        rotblock0 = (gate_[1][0] == -gate_[0][1])
        rotblock1 = (gate_[2][3] == -gate_[3][2])
        self.assertTrue(rotblock0 and rotblock1)

    def test_level_gate_1_sincosrow0(self):
        sigma = 3.5
        mu = 5.0
        gate_ = self.gauss.level_gate(sigma, mu, 1)
        self.assertEqual((gate_[0][0])**2 + (gate_[0][1])**2, 1.)

    def test_level_gate_1_sincosrow1(self):
        sigma = 3.5
        mu = 5.0
        gate_ = self.gauss.level_gate(sigma, mu, 1)
        self.assertEqual((gate_[1][0])**2 + (gate_[1][1])**2, 1.)

    def test_level_gate_1_sincosrow2(self):
        sigma = 3.5
        mu = 5.0
        gate_ = self.gauss.level_gate(sigma, mu, 1)
        self.assertEqual((gate_[2][2])**2 + (gate_[2][3])**2, 1.)

    def test_level_gate_1_sincosrow3(self):
        sigma = 3.5
        mu = 5.0
        gate_ = self.gauss.level_gate(sigma, mu, 1)
        self.assertEqual((gate_[3][2])**2 + (gate_[3][3])**2, 1.)

    def test_level_gate_1_zeroblock0(self):
        sigma = 3.5
        mu = 5.0
        gate_ = self.gauss.level_gate(sigma, mu, 1)
        self.assertTrue(gate_[0][2] == gate_[0][3] == gate_[1][2] == gate_[1][3])

    def test_level_gate_1_zeroblock1(self):
        sigma = 3.5
        mu = 5.0
        gate_ = self.gauss.level_gate(sigma, mu, 1)
        self.assertTrue(gate_[2][0] == gate_[2][1] == gate_[3][0] == gate_[3][1])


if __name__ == "__main__":
    unittest.main()
