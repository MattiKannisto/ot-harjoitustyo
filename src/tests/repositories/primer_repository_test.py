import unittest
from repositories.primer_repository import primer_repository
import database_initialization


class TestprimerRepository(unittest.TestCase):
    def setUp(self):
        database_initialization.initialize()
        self.primer_repository = primer_repository
        self.name_1 = "test primer 1"
        self.name_2 = "test primer 2"
        self.sequence_1 = "ATATGTCGTGACATGTAGTA"
        self.sequence_2 = "ATCGATGTGGTAGTTATACA"
        self.template_dna_name = "test DNA fragment"

    def test_create(self):
        self.assertEqual(self.primer_repository.find_by_sequence_and_template_dna_name(
            self.sequence_1, self.template_dna_name), None)
        self.primer_repository.create(
            self.name_1, self.sequence_1, self.template_dna_name)
        self.assertEqual(self.primer_repository.find_by_sequence_and_template_dna_name(
            self.sequence_1, self.template_dna_name)[0], self.name_1)

    def test_count_by_template_dna_name_returns_correct_value(self):
        self.primer_repository.create(
            self.name_1, self.sequence_1, self.template_dna_name)
        self.primer_repository.create(
            self.name_2, self.sequence_2, self.template_dna_name)
        self.assertEqual(self.primer_repository.count_by_template_dna_name(
            self.template_dna_name), 2)

    def test_count_by_name_prefix_and_infix_returns_correct_values(self):
        values = []
        values.append(
            self.primer_repository.count_by_name_prefix_and_infix(self.name_1))
        self.primer_repository.create(
            self.name_1 + "_1", self.sequence_1, self.template_dna_name)
        values.append(
            self.primer_repository.count_by_name_prefix_and_infix(self.name_1))
        self.primer_repository.create(
            self.name_1 + "_2", self.sequence_2, self.template_dna_name)
        values.append(
            self.primer_repository.count_by_name_prefix_and_infix(self.name_1))

        self.assertEqual(values, [0, 1, 2])

    def test_find_all_by_template_dna_name_returns_correct_value(self):
        self.primer_repository.create(
            self.name_1 + "_1", self.sequence_1, self.template_dna_name)
        self.primer_repository.create(
            self.name_1 + "_2", self.sequence_2, self.template_dna_name)
        self.assertEqual(len(self.primer_repository.find_all_by_template_dna_name(
            self.template_dna_name)), 2)
