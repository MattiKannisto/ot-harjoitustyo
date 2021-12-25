import os
import unittest
from services.protein_service import ProteinService


class TestProteinService(unittest.TestCase):
    def setUp(self):
        self.protein_service = ProteinService()
        self.name = "test dna fragment name"
        self.owner_name = "test owner name"
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.valid_dna_sequence_translation = "MKKTKIVCTIGPKTESEEMLAKM"
        self.dna_sequence_that_doesnt_start_with_start_codon = "AAAATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.start_codon = "ATG"
        self.stop_codon = "TAA"

        self.notification_that_no_directory = [
            "Please set a working directory in the settings first!", "red"]
        self.notification_that_no_for_strand = [
            "Forward strand of the DNA fragment has not been defined!", "red"]

        self.test_directory = "./src/tests/temporary_test_directory"

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
        self.assertEqual(self.protein_service._translate(
            self.valid_dna_sequence), self.valid_dna_sequence_translation)

    def test_translate_ignores_codons_before_start_codon(self):
        self.assertEqual(self.protein_service._translate(
            self.dna_sequence_that_doesnt_start_with_start_codon), self.valid_dna_sequence_translation)

    def test_directory_exists_after_create_directory_if_not_existing(self):
        self.assertEqual(os.path.isdir(self.test_directory), False)
        self.protein_service._create_directory_if_not_existing(
            self.test_directory)
        self.assertEqual(os.path.isdir(self.test_directory), True)
        os.rmdir(self.test_directory)

    def test_translation_file_exists_after_write_translation_to_file(self):
        path = os.path.join(self.test_directory,
                            self.name + "_translation.csv")
        self.assertEqual(os.path.isfile(path), False)
        self.protein_service._write_to_file(
            self.test_directory, self.name, self.valid_dna_sequence_translation)
        self.assertEqual(os.path.isfile(path), True)
        os.remove(path)
        os.rmdir(self.test_directory)

    def test_attempt_translation_and_return_notification_returns_correct_notification_if_no_directory(self):
        notification = self.protein_service.attempt_translation_and_return_notification(
            self.name, self.valid_dna_sequence, None)
        self.assertEqual(notification, self.notification_that_no_directory)

    def test_attempt_translation_and_return_notification_returns_correct_notification_if_no_forward_strand(self):
        notification = self.protein_service.attempt_translation_and_return_notification(
            self.name, None, ".")
        self.assertEqual(notification, self.notification_that_no_for_strand)
