import unittest
from services.primer_service import PrimerService


class TestPrimerService(unittest.TestCase):
    def setUp(self):
        self.directory = "/test/directory"
        self.length = 20
        self.gc_content = 0.5
        self.primer_service = PrimerService(
            self.directory, self.length, self.gc_content)

    def test_newly_created_primer_service_has_correct_primer_length(self):
        self.assertEqual(self.primer_service.length, self.length)
