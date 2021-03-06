import unittest
from services.dna_fragment_service import DnaFragmentService


class MockUpDnaFragmentRepository:
    def __init__(self):
        self.dna_fragments = []

    def create(self, name, for_strand, rev_strand, owner_name):
        self.dna_fragments.append(
            (name, for_strand, rev_strand, owner_name))

    def find_by_name_and_owner_name(self, name, owner_name):
        for dna_fragment in self.dna_fragments:
            if dna_fragment[0] == name and dna_fragment[3] == owner_name:
                return dna_fragment
        return None

    def find_by_name(self, name):
        for dna_fragment in self.dna_fragments:
            if dna_fragment[0] == name:
                return dna_fragment
        return None

    def find_all_by_owner_name(self, owner_name):
        found_dna_fragments = []
        for dna_fragment in self.dna_fragments:
            if dna_fragment[3] == owner_name:
                found_dna_fragments.append(dna_fragment)
        return found_dna_fragments


class TestDnaFragmentService(unittest.TestCase):
    def setUp(self):
        self.dna_fragment_service = DnaFragmentService(MockUpDnaFragmentRepository())
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.invalid_dna_sequence = "FTGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.dna_fragment_name = "test_dna_fragment"
        self.dna_fragment_name_2 = "test_dna_fragment 2"
        self.valid_dna_sequence_2 = "ATGAAAAAGACCAAAATTGTTTG"
        self.owner_name = "test username"
        self.notification_that_dna_fragment_already_exists = [
            "You already have a DNA fragment with this name!", "red"]
        self.notification_that_dna_sequence_contains_invalid_letters = [
            "Invalid DNA sequence! The sequence should contain only letters 'A', 'T', 'G' and 'C'", "red"]
        self.notification_that_dna_fragment_successfully_added = [
            "DNA fragment '" + self.dna_fragment_name + "' added", "green"]

    def test_incorrect_letters_found_returns_false_with_valid_dna_sequence(self):
        self.assertEqual(self.dna_fragment_service._incorrect_letters_found(
            self.valid_dna_sequence), False)

    def test_incorrect_letters_found_returns_true_with_invalid_dna_sequence(self):
        self.assertEqual(self.dna_fragment_service._incorrect_letters_found(
            self.invalid_dna_sequence), True)

    def test_try_to_create_new_dna_fragment_and_return_notification_returns_correct_notification_if_dna_fragment_already_exists(self):
        self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence, self.owner_name)
        notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence, self.owner_name)
        self.assertEqual(
            notification, self.notification_that_dna_fragment_already_exists)

    def test_try_to_create_new_dna_fragment_and_return_notification_returns_correct_notification_if_sequence_is_invalid(self):
        notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.invalid_dna_sequence, self.owner_name)
        self.assertEqual(
            notification, self.notification_that_dna_sequence_contains_invalid_letters)

    def test_try_to_create_new_dna_fragment_and_return_notification_returns_correct_notification_if_dna_fragment_can_be_added(self):
        notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence, self.owner_name)
        self.assertEqual(
            notification, self.notification_that_dna_fragment_successfully_added)

    def test_get_all_dna_fragments_by_owner_name(self):
        self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence, self.owner_name)
        self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name_2, self.valid_dna_sequence_2, self.owner_name)
        dna_fragments = self.dna_fragment_service.get_all_dna_fragments_by_owner_name(
            self.owner_name)
        self.assertEqual(len(dna_fragments), 2)

    def test_get_dna_fragment_by_name_returns_correct_dna_fragment(self):
        self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            self.dna_fragment_name, self.valid_dna_sequence, self.owner_name)
        self.assertEqual(self.dna_fragment_service.get_dna_fragment_by_name_and_owner_name(
            self.dna_fragment_name, self.owner_name).name, self.dna_fragment_name)

    def test_get_dna_fragment_by_name_returns_none_if_no_dna_fragments_have_been_added_to_database(self):
        self.assertEqual(self.dna_fragment_service.get_dna_fragment_by_name_and_owner_name(
            self.dna_fragment_name, self.owner_name), None)
