import os
import csv
from pathlib import Path

CODON_CHART = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R',
               'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
CODON_LENGTH = 3
START_CODON = 'ATG'
STOP_CODONS = ['TAA', 'TAG']


class ProteinService:
    """A class responsible for protein related application logic
    """

    def __init__(self):
        """A constructor for creating a new ProteinService object
        """

        self.start_codon_encountered = False

    def attempt_translation_and_return_notification(self, dna_fragment, directory):
        """A method for attempting to translate the DNA fragment into a protein and returning a notification on the failure or successfulness of this action

        Args:
            dna_fragment: The DNA fragment as a DnaFragment object
            directory: Directory into which the output file containing the translation will be saved

        Returns:
            An array of two strings of characters containing a notification text and a color of the notification if the DNA fragment's sequence is not None
        """

        if dna_fragment.sequence:
            translation = self.translate(dna_fragment.sequence)
            self.write_translation_to_file(
                directory + "/translations", translation)
            return ["Translation of the DNA fragment '" + dna_fragment.name + "' added to folder " + directory + "/translations", "yellow"]

    def translate(self, dna_sequence):
        if len(dna_sequence) < CODON_LENGTH or self.is_stop_codon(dna_sequence[:CODON_LENGTH]):
            self.start_codon_encountered = False
            return ""
        if self.start_codon_encountered:
            return CODON_CHART[dna_sequence[:CODON_LENGTH]] + self.translate(dna_sequence[CODON_LENGTH:])
        if self.is_start_codon(dna_sequence[:CODON_LENGTH]):
            self.start_codon_encountered = True
            return self.translate(dna_sequence)
        return self.translate(dna_sequence[CODON_LENGTH:])

    def write_translation_to_file(self, directory_name, translation):
        if not os.path.isdir(directory_name):
            Path(os.path.join(directory_name)).mkdir()
        Path(os.path.join(directory_name, "translation.csv")).touch()
        with open(os.path.join(directory_name, "translation.csv"), 'w') as csvfile:
            csvfile.seek(0)
            csv.writer(csvfile, delimiter=',').writerow([translation])

    def is_start_codon(self, codon):
        return codon == START_CODON

    def is_stop_codon(self, codon):
        return codon in STOP_CODONS
