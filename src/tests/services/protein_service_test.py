import unittest
from services.protein_service import ProteinService


class TestProteinService(unittest.TestCase):
    def setUp(self):
        self.protein_service = ProteinService()
        # Beginning of E. coli pykF gene (NCBI Ref: NC_000913.3)
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.start_codon = "ATG"
        self.stop_codon = "TAA"

    def test_newly_created_protein_service_has_not_encountered_a_start_codon(self):
        self.assertEqual(self.protein_service.start_codon_encountered, False)

    def test_protein_service_has_not_encountered_a_start_codon_is_returned_to_false_after_translation(self):
        self.protein_service.translate(self.valid_dna_sequence)
        self.assertEqual(self.protein_service.start_codon_encountered, False)

    def test_is_start_codon_returns_true_with_correct_codon(self):
        self.assertEqual(self.protein_service.is_start_codon(
            self.start_codon), True)

    def test_is_start_codon_returns_false_with_incorrect_codon(self):
        self.assertEqual(self.protein_service.is_start_codon(
            self.stop_codon), False)

    def test_is_stop_codon_returns_true_with_correct_codon(self):
        self.assertEqual(
            self.protein_service.is_stop_codon(self.stop_codon), True)

    def test_is_stop_codon_returns_true_with_incorrect_codon(self):
        self.assertEqual(self.protein_service.is_stop_codon(
            self.start_codon), False)
