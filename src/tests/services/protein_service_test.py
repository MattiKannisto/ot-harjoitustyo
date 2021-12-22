import unittest
from services.protein_service import ProteinService


class TestProteinService(unittest.TestCase):
    def setUp(self):
        self.protein_service = ProteinService()
        # Beginning of E. coli pykF gene (NCBI Ref: NC_000913.3)
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.dna_sequence_that_doesnt_start_with_start_codon = "AAAATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.dna_sequence_without_start_codon = "AAATTTAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGGGGTTAGCTAAATTTC"
        self.valid_dna_sequence_translation = "MKKTKIVCTIGPKTESEEMLAKM"
        self.start_codon = "ATG"
        self.stop_codon = "TAA"

        self.notification_that_no_directory = ["Please set a working directory in the settings first!", "red"]
        self.notification_that_couldnt_translate = ["Could not be translated, no start codon found!", "yellow"]

    def test_newly_created_protein_service_has_not_encountered_a_start_codon(self):
        self.assertEqual(self.protein_service._start_codon_encountered, False)

    def test_protein_service_has_not_encountered_a_start_codon_is_returned_to_false_after_translation(self):
        self.protein_service._translate(self.valid_dna_sequence)
        self.assertEqual(self.protein_service._start_codon_encountered, False)

    def test_is_start_codon_returns_true_with_correct_codon(self):
        self.assertEqual(self.protein_service._is_start_codon(
            self.start_codon), True)

    def test_is_start_codon_returns_false_with_incorrect_codon(self):
        self.assertEqual(self.protein_service._is_start_codon(
            self.stop_codon), False)

    def test_is_stop_codon_returns_true_with_correct_codon(self):
        self.assertEqual(
            self.protein_service._is_stop_codon(self.stop_codon), True)

    def test_is_stop_codon_returns_true_with_incorrect_codon(self):
        self.assertEqual(self.protein_service._is_stop_codon(
            self.start_codon), False)

    def test_translate_produces_correct_protein_sequence_from_dna_sequence(self):
        self.assertEqual(self.protein_service._translate(self.valid_dna_sequence), self.valid_dna_sequence_translation)

    def test_translate_ignores_codons_before_start_codon(self):
        self.assertEqual(self.protein_service._translate(self.dna_sequence_that_doesnt_start_with_start_codon), self.valid_dna_sequence_translation)

#    def test_attempt_translation_and_return_notification_without_directory(self):
#        self.protein_service.attempt_translation_and_return_notification()