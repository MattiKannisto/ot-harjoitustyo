import unittest
from services.primer_service import PrimerService


class TestPrimerService(unittest.TestCase):
    def setUp(self):
        self.directory = "/test/directory"
        self.length = 20
        self.gc_content = 0.5
        self.primer_service = PrimerService(self.directory, self.length, self.gc_content)
        self.sequence_with_gc_lock = "ATATAATCG"
        self.sequence_without_gc_lock = "GCCGAATATTA"

    def test_newly_created_primer_service_has_correct_primer_length(self):
        self.assertEqual(self.primer_service.length, self.length)

    def test_no_gc_lock_returns_false_if_gc_lock(self):
        self.assertEqual(self.primer_service._no_gc_lock(self.sequence_with_gc_lock), False)

    def test_no_gc_lock_returns_true_if_no_gc_lock(self):
        self.assertEqual(self.primer_service._no_gc_lock(self.sequence_without_gc_lock), True)
