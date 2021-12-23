import unittest
from entities.primer import Primer


class TestPrimer(unittest.TestCase):
    def setUp(self):
        self.name = "test_primer_1"
        self.sequence = "ATTAGTCGATGATTATACGG"
        self.template_dna_name = "valid_dna_fragment_name"
        self.primer = Primer(self.name, self.sequence, self.template_dna_name)

    def test_newly_created_primer_has_correct_name(self):
        self.assertEqual(self.primer.name, self.name)

    def test_newly_created_primer_has_correct_sequence(self):
        self.assertEqual(self.primer.sequence,
                         self.sequence)

    def test_newly_created_primer_has_correct_template_dna_name(self):
        self.assertEqual(self.primer.template_dna_name,
                         self.template_dna_name)
