import unittest
from entities.dna_fragment import DnaFragment


class TestDnaFragment(unittest.TestCase):
    def setUp(self):
        # Beginning of E. coli pykF gene (NCBI Ref: NC_000913.3)
        self.forward_strand = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"
        self.name = "Valid DNA fragment name"
        self.reverse_strand = "GCATTTTAGCTAACATCTCTTCAGATTCGGTTTTCGGTCCGATGGTGCAAACAATTTTGGTCTTTTTCAT"
        self.owner = "test_username"

        self.dna_fragment = DnaFragment(
            self.name, self.forward_strand, self.reverse_strand, self.owner)

    def test_newly_created_dna_fragment_has_correct_name(self):
        self.assertEqual(self.dna_fragment.name,
                         self.name)

    def test_newly_created_dna_fragment_has_correct_forward_strand(self):
        self.assertEqual(self.dna_fragment.forward_strand,
                         self.forward_strand)

    def test_newly_created_dna_fragment_has_correct_reverse_strand(self):
        self.assertEqual(self.dna_fragment.reverse_strand,
                         self.reverse_strand)

    def test_newly_created_dna_fragment_has_correct_owner(self):
        self.assertEqual(self.dna_fragment.owner,
                         self.owner)
