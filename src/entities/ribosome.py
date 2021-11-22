AMINO_ACID_CORRESPONDING_TO_CODON = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
CODON_LENGTH = 3

class Ribosome:
    def __init__(self):
        self.start_codon_encountered = False

    def translate(self, dna_sequence):
        if len(dna_sequence) < CODON_LENGTH or self.is_stop_codon(dna_sequence[:CODON_LENGTH]):
            self.start_codon_encountered = False
            return ""
        elif self.start_codon_encountered:
            return AMINO_ACID_CORRESPONDING_TO_CODON[dna_sequence[:CODON_LENGTH]] + self.translate(dna_sequence[CODON_LENGTH:])
        else:
            if self.is_start_codon(dna_sequence[:CODON_LENGTH]):
                self.start_codon_encountered = True
                return self.translate(dna_sequence)
            else:
                return self.translate(dna_sequence[CODON_LENGTH:])

    def is_start_codon(self, codon):
        return codon == "ATG"

    def is_stop_codon(self, codon):
        return codon == "TAA" or codon == "TAG"