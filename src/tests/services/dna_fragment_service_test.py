import unittest
from services.dna_fragment_service import DnaFragmentService
import database_initialization


class TestDnaFragmentService(unittest.TestCase):
    def setUp(self):
        database_initialization.initialize()
        self.dna_fragment_service = DnaFragmentService()
        # Beginning of E. coli pykF gene (NCBI Ref: NC_000913.3)
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.invalid_dna_sequence = "FTGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.dna_fragment_name = "test_dna_fragment"
        self.notification_that_dna_fragment_already_exists = [
            "You already have a DNA fragment with this name!", "red"]
        self.notification_that_dna_sequence_contains_invalid_letters = [
            "Invalid DNA sequence! The sequence should contain only letters 'A', 'T', 'G' and 'C'", "red"]
        self.notification_that_dna_fragment_successfully_added = [
            "DNA fragment '" + self.dna_fragment_name + "' added", "green"]

    def test_incorrect_letters_found_returns_false_with_valid_dna_sequence(self):
        self.assertEqual(self.dna_fragment_service.incorrect_letters_found(
            self.valid_dna_sequence), False)

    def test_incorrect_letters_found_returns_true_with_invalid_dna_sequence(self):
        self.assertEqual(self.dna_fragment_service.incorrect_letters_found(
            self.invalid_dna_sequence), True)

    def test_incorrect_letters_found_returns_none_if_no_dna_sequence_has_been_given(self):
        self.assertEqual(
            self.dna_fragment_service.incorrect_letters_found(None), None)

    def test_try_to_create_new_dna_fragment_and_return_notification_returns_correct_notification_if_dna_fragment_already_exists(self):
        self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence)
        notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence)
        self.assertEqual(
            notification, self.notification_that_dna_fragment_already_exists)

    def test_try_to_create_new_dna_fragment_and_return_notification_returns_correct_notification_if_sequence_is_invalid(self):
        notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.invalid_dna_sequence)
        self.assertEqual(
            notification, self.notification_that_dna_sequence_contains_invalid_letters)

    def test_try_to_create_new_dna_fragment_and_return_notification_returns_correct_notification_if_dna_fragment_can_be_added(self):
        notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence)
        self.assertEqual(
            notification, self.notification_that_dna_fragment_successfully_added)

    def test_get_dna_fragment_by_name_returns_correct_dna_fragment(self):
        self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence)
        self.assertEqual(self.dna_fragment_service.get_dna_fragment_by_name(
            self.dna_fragment_name).name, self.dna_fragment_name)

    def test_get_dna_fragment_by_name_returns_none_if_no_dna_fragments_have_been_added_to_database(self):
        self.assertEqual(self.dna_fragment_service.get_dna_fragment_by_name(
            self.dna_fragment_name), None)
