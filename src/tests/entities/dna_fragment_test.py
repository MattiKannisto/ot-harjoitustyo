import unittest
from entities.dna_fragment import DnaFragment


class TestDnaFragment(unittest.TestCase):
    def setUp(self):
        self.for_strand = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.name = "Valid DNA fragment name"
        self.rev_strand = "GCATTTTAGCTAACATCTCTTCAGATTCGGTTTTCGGTCCGATGGTGCAAACAATTTTGGTCTTTTTCAT"
        self.owner_name = "test_username"

        self.dna_fragment = DnaFragment(
            self.name, self.for_strand, self.rev_strand, self.owner_name)

    def test_newly_created_dna_fragment_has_correct_name(self):
        self.assertEqual(self.dna_fragment.name, self.name)

    def test_newly_created_dna_fragment_has_correct_for_strand(self):
        self.assertEqual(self.dna_fragment.for_strand, self.for_strand)

    def test_newly_created_dna_fragment_has_correct_rev_strand(self):
        self.assertEqual(self.dna_fragment.rev_strand, self.rev_strand)

    def test_newly_created_dna_fragment_has_correct_owner_name(self):
        self.assertEqual(self.dna_fragment.owner_name, self.owner_name)
