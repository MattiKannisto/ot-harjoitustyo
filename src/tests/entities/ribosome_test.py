import unittest
from entities.ribosome import Ribosome


class TestRibosome(unittest.TestCase):
    def setUp(self):
        self.ribosome = Ribosome()
        # Beginning of E. coli pykF gene (NCBI Ref: NC_000913.3)
        self.valid_dna_sequence = "ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGC"

    def test_newly_created_ribosome_has_not_encountered_a_start_codon(self):
        self.assertEqual(self.ribosome.start_codon_encountered, False)

    def test_ribosome_has_not_encountered_a_start_codon_is_returned_to_false_after_translation(self):
        self.ribosome.translate(self.valid_dna_sequence)
        self.assertEqual(self.ribosome.start_codon_encountered, False)
