import os
import csv
from pathlib import Path

CODON_CHART = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S',
               'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 'TGT': 'C', 'TGC': 'C',
               'TGA': '*', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P',
               'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
               'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
               'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N',
               'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V',
               'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
               'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
               'GGG': 'G'}
CODON_LENGTH = 3
START_CODON = 'ATG'
STOP_CODONS = ['TAA', 'TAG']


class ProteinService:
    """A class responsible for protein related application logic
    """

    def __init__(self):
        """A constructor for creating a new ProteinService object
        """

    def attempt_translation_and_return_notification(self, name, for_strand, directory):
        """A method for attempting to translate the DNA fragment into a protein and returning
           a notification on the failure or successfulness of this action. The protein coding
           sequence is assumed to be in the forward strand of the DNA fragment as it is common
           practice in molecular biology

        Args:
            name: Name of the DNA fragment as string
            for_strand: Forward strand of the DNA fragment as string
            directory: Directory into which the output file containing the translation is saved

        Returns:
            An array of two strings containing a notification text and a color of the notification
        """
        if not directory:
            return ["Please set a working directory in the settings first!", "red"]
        if not os.access(directory, os.W_OK):
            return ["You do not have the right to write to a file in this directory!", "red"]
        if not for_strand:
            return ["Forward strand of the DNA fragment has not been defined!", "red"]
        translation = self._translate(for_strand)
        if not translation:
            return ["Could not be translated, no start codon found!", "yellow"]
        self._write_to_file(directory + "/translations", name, translation)
        return ["Translation of the DNA fragment '" + name
                + "' added to folder " + directory + "/translations", "green"]

    def _translate(self, sequence, start_codon_encountered=False):
        if len(sequence) < CODON_LENGTH or self._is_stop_codon(sequence[:CODON_LENGTH]):
            return ""
        if start_codon_encountered:
            return CODON_CHART[sequence[:CODON_LENGTH]] + self._translate(sequence[CODON_LENGTH:],
                                                                          start_codon_encountered)
        if self._is_start_codon(sequence[:CODON_LENGTH]):
            start_codon_encountered = True
            return self._translate(sequence, start_codon_encountered)
        return self._translate(sequence[CODON_LENGTH:],  start_codon_encountered)

    def _write_to_file(self, directory, name, translation):
        self._create_directory_if_not_existing(directory)
        file_name = name + "_translation.csv"
        Path(os.path.join(directory, file_name)).touch()
        with open(os.path.join(directory, file_name), 'w', encoding='utf-8') as file:
            file.seek(0)
            csv.writer(file, delimiter=',').writerow([translation])

    def _create_directory_if_not_existing(self, directory):
        if not os.path.isdir(directory):
            Path(os.path.join(directory)).mkdir()

    def _is_start_codon(self, codon):
        return codon == START_CODON

    def _is_stop_codon(self, codon):
        return codon in STOP_CODONS
