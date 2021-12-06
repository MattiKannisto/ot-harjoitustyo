import unittest
from entities.primer import Primer


class TestPrimer(unittest.TestCase):
    def setUp(self):
        self.name = "test_primer_1"
        self.sequence_with_length_of_20 = "ATTAGTCGATGATTATACGG"
        self.primer = Primer(self.name, self.sequence_with_length_of_20)

    def test_get_name_returns_correct_string(self):
        self.assertEqual(self.primer.get_name(), self.name)

    def test_get_sequence_returns_correct_string(self):
        self.assertEqual(self.primer.get_sequence(), self.sequence_with_length_of_20)

    def test_get_length_returns_correct_integer(self):
        self.assertEqual(self.primer.get_length(), 20)
