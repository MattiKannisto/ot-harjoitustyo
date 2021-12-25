import unittest
from services.primer_service import PrimerService


class MockUpprimerRepository:
    def __init__(self):
        self.primers = []

    def create(self, name, sequence, template_dna_name):
        self.primers.append((name, sequence, template_dna_name))

    def count_by_name_prefix_and_infix(self, prefix_and_infix):
        count = 0
        for primer in self.primers:
            if prefix_and_infix in primer[0]:
                count += 1
        return count

    def count_by_template_dna_name(self, template_dna_name):
        count = 0
        for primer in self.primers:
            if template_dna_name == primer[2]:
                count += 1
        return count

    def find_by_sequence_and_template_dna_name(self, sequence, template_dna_name):
        count = 0
        for primer in self.primers:
            if (template_dna_name == primer[2]) and (sequence == primer[1]):
                count += 1
        return count

    def find_all_by_template_dna_name(self, template_dna_name):
        primers = []
        for primer in self.primers:
            if template_dna_name == primer[2]:
                primers.append(primer)
        return primers


class TestPrimerService(unittest.TestCase):
    def setUp(self):
        self.directory = "/test/directory"
        self.length = 20
        self.gc_content = 0.5
        self.primer_service = PrimerService(MockUpprimerRepository())
        self.sequence_with_gc_lock = "ATATAATCG"
        self.sequence_without_gc_lock = "GCCGAATATGA"
        self.sequence_with_gc_content_50_percent = "AAAAACCCCC"
        self.sequence_with_gc_content_40_percent = "AAAAAACCCC"

    def test_no_gc_lock_returns_false_if_gc_lock(self):
        self.assertEqual(self.primer_service._no_gc_lock(
            self.sequence_with_gc_lock), False)

    def test_no_gc_lock_returns_true_if_no_gc_lock(self):
        self.assertEqual(self.primer_service._no_gc_lock(
            self.sequence_without_gc_lock), True)

    def test_gc_content_incorrect_returns_true_if_gc_content_differs(self):
        value = self.primer_service._gc_content_incorrect(
            self.gc_content, self.sequence_with_gc_content_40_percent)
        self.assertEqual(value, True)

    def test_gc_content_incorrect_returns_true_if_gc_content_same(self):
        value = self.primer_service._gc_content_incorrect(
            self.gc_content, self.sequence_with_gc_content_50_percent)
        self.assertEqual(value, False)

    def test_multiple_occurrences_returns_true_if_dna_sequence_contains_primer_sequence_twice(self):
        self.assertEqual(self.primer_service._multiple_occurrences(self.sequence_with_gc_content_50_percent +
                         self.sequence_with_gc_content_50_percent, self.sequence_with_gc_content_50_percent), True)

    def test_multiple_occurrences_returns_false_if_dna_sequence_contains_primer_sequence_once(self):
        self.assertEqual(self.primer_service._multiple_occurrences(self.sequence_with_gc_content_40_percent +
                         self.sequence_with_gc_content_50_percent, self.sequence_with_gc_content_50_percent), False)
