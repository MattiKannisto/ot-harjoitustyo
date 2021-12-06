import unittest
from entities.dna_fragment import DnaFragment


class TestDnaFragment(unittest.TestCase):
    def setUp(self):
        # Beginning of E. coli pykF gene (NCBI Ref: NC_000913.3)
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.valid_dna_fragment_name = "Valid DNA fragment name"
        self.valid_dna_sequence_reverse_complement = "GCATTTTAGCTAACATCTCTTCAGATTCGGTTTTCGGTCCGATGGTGCAAACAATTTTGGTCTTTTTCAT"

        self.valid_dna_fragment = DnaFragment(
            self.valid_dna_fragment_name, self.valid_dna_sequence)
        self.dna_fragment_with_none_as_name_and_sequence = DnaFragment()

    def test_get_name_returns_correct_string(self):
        self.assertEqual(self.valid_dna_fragment.get_name(),
                         self.valid_dna_fragment_name)

    def test_get_name_returns_none_if_name_has_not_been_given(self):
        self.assertEqual(self.dna_fragment_with_none_as_name_and_sequence.get_name(), None)

    def test_get_sequence_returns_correct_string(self):
        self.assertEqual(self.valid_dna_fragment.get_sequence(),
                         self.valid_dna_sequence)

    def test_get_sequence_returns_none_if_sequence_has_not_been_given(self):
        self.assertEqual(self.dna_fragment_with_none_as_name_and_sequence.get_sequence(), None)

    def test_get_reverse_complement_returns_correct_dna_sequence(self):
        self.assertEqual(self.valid_dna_fragment.get_reverse_complement(
        ), self.valid_dna_sequence_reverse_complement)

    def test_get_reverse_complement_returns_none_if_no_dna_sequence_has_been_given(self):
        self.assertEqual(self.dna_fragment_with_none_as_name_and_sequence.get_reverse_complement(), None)