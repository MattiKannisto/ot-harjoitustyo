import unittest
from repositories.dna_fragment_repository import dna_fragment_repository
import database_initialization


class TestDnaFragmentRepository(unittest.TestCase):
    def setUp(self):
        database_initialization.initialize()
        self.dna_fragment_repository = dna_fragment_repository
        self.name_1 = "test dna_fragment 1"
        self.name_2 = "test dna_fragment 2"
        self.for_strand_1 = "ATATGTCGTGACATGTAGTA"
        self.for_strand_2 = "ATCGATGTGGTAGTTATACA"
        self.rev_strand_1 = "TACTACATGTCACGACATAT"
        self.rev_strand_2 = "TGTATAACTACCACATCGAT"
        self.owner_name = "test username"

    def test_create_adds_new_dna_fragment_to_database(self):
        self.assertEqual(
            len(self.dna_fragment_repository.find_all_by_owner_name(self.owner_name)), 0)
        self.dna_fragment_repository.create(
            self.name_1, self.for_strand_1, self.rev_strand_1, self.owner_name)
        self.assertEqual(
            len(self.dna_fragment_repository.find_all_by_owner_name(self.owner_name)), 1)

    def test_find_by_name_and_owner_name_works_if_fragment_added_to_database(self):
        self.assertEqual(self.dna_fragment_repository.find_by_name_and_owner_name(
            self.name_1, self.owner_name), None)
        self.dna_fragment_repository.create(
            self.name_1, self.for_strand_1, self.rev_strand_1, self.owner_name)
        self.assertEqual(self.dna_fragment_repository.find_by_name_and_owner_name(
            self.name_1, self.owner_name)[0], self.name_1)

    def test_find_all_by_owner_name_returns_correct_value(self):
        values = []
        values.append(
            len(self.dna_fragment_repository.find_all_by_owner_name(self.owner_name)))
        self.dna_fragment_repository.create(
            self.name_1, self.for_strand_1, self.rev_strand_1, self.owner_name)
        values.append(
            len(self.dna_fragment_repository.find_all_by_owner_name(self.owner_name)))
        self.dna_fragment_repository.create(
            self.name_2, self.for_strand_2, self.rev_strand_2, self.owner_name)
        values.append(
            len(self.dna_fragment_repository.find_all_by_owner_name(self.owner_name)))
        self.assertEqual(values, [0, 1, 2])
