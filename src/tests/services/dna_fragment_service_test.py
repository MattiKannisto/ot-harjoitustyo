import unittest
from services.dna_fragment_service import DnaFragmentService


class TestDnaFragment(unittest.TestCase):
    def setUp(self):
        self.dna_fragment_service = DnaFragmentService()
        # Beginning of E. coli pykF gene (NCBI Ref: NC_000913.3)
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.invalid_dna_sequence = "FTGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"

    def test_incorrect_letters_found_returns_false_with_valid_dna_sequence(self):
        self.assertEqual(self.dna_fragment_service.incorrect_letters_found(self.valid_dna_sequence), False)

    def test_incorrect_letters_found_returns_true_with_invalid_dna_sequence(self):
        self.assertEqual(self.dna_fragment_service.incorrect_letters_found(self.invalid_dna_sequence), True)

    def test_incorrect_letters_found_returns_none_if_no_dna_sequence_has_been_given(self):
        self.assertEqual(self.dna_fragment_service.incorrect_letters_found(None), None)
