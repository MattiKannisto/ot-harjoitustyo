import unittest
from services.primer_service import PrimerService


class TestPrimerService(unittest.TestCase):
    def setUp(self):
        self.primer_service = PrimerService()

    def test_newly_created_primer_service_has_primer_length_of_20(self):
        self.assertEqual(self.primer_service.length, 20)
