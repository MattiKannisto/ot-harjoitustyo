import unittest
from entities.dna_fragment import DnaFragment


class TestDnaFragment(unittest.TestCase):
    def setUp(self):
        # Beginning of E. coli pykF gene (NCBI Ref: NC_000913.3)
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.valid_dna_fragment_name = "Valid DNA fragment name"
        self.invalid_dna_sequence_with_an_incorrect_first_letter = "FTGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.valid_dna_sequence_reverse_complement = "GCATTTTAGCTAACATCTCTTCAGATTCGGTTTTCGGTCCGATGGTGCAAACAATTTTGGTCTTTTTCAT"

        self.valid_dna_fragment = DnaFragment(
            self.valid_dna_fragment_name, self.valid_dna_sequence)
        self.invalid_dna_fragment_with_invalid_sequence = DnaFragment(
            self.valid_dna_fragment_name, self.invalid_dna_sequence_with_an_incorrect_first_letter)

    def test_get_name_returns_correct_string(self):
        self.assertEqual(self.valid_dna_fragment.get_name(), self.valid_dna_fragment_name)

    def test_get_sequence_returns_correct_string(self):
        self.assertEqual(self.valid_dna_fragment.get_sequence(), self.valid_dna_sequence)

    def test_dna_fragment_with_valid_dna_sequence_can_be_created(self):
        self.assertEqual(self.valid_dna_fragment.sequence,
                         self.valid_dna_sequence)

    def test_get_reverse_complement_returns_correct_dna_sequence(self):
        self.assertEqual(self.valid_dna_fragment.get_reverse_complement(
        ), self.valid_dna_sequence_reverse_complement)

    def test_incorrect_letters_found_returns_false_with_valid_dna_sequence(self):
        self.assertEqual(
            self.valid_dna_fragment.incorrect_letters_found(), False)

    def test_incorrect_letters_found_returns_true_with_invalid_dna_sequence(self):
        self.assertEqual(
            self.invalid_dna_fragment_with_invalid_sequence.incorrect_letters_found(), True)
