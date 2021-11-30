import os
import csv
from pathlib import Path
from entities.primer import Primer


class PrimerService:
    def __init__(self):
        self.length = 20
        self.directory_name = os.path.dirname(__file__)
        with open(os.path.join(self.directory_name, "..", "..", "data", "settings.csv"), "r") as csvfile_0:
            reader = csv.reader(csvfile_0, delimiter=',')
            for row in reader:
                self.length = int(row[0])
                self.gc_content = float(row[1])

    def set_sequencing_primer_length(self, length):
        self.length = length

    def set_directory_name(self, user_given_directory):
        self.directory_name = user_given_directory

    def generate_sequencing_primers(self, dna_sequence):
        sequencing_primers = []
        for letter_index in range(len(dna_sequence)-(self.length-1)):
            sequencing_primer_candidate = dna_sequence[letter_index:(
                letter_index + self.length)]
            if self.gc_content_is_incorrect(sequencing_primer_candidate) or self.gc_lock_does_not_exist(sequencing_primer_candidate) or self.multiple_occurrences_in_dna_sequence(dna_sequence, sequencing_primer_candidate):
                continue
            sequencing_primers.append(sequencing_primer_candidate)
        self.write_sequencing_primers_to_file(sequencing_primers)
        return sequencing_primers

    def gc_content_is_incorrect(self, primer):
        return (primer.count('G') + primer.count('C')) != self.length * self.gc_content

    def gc_lock_does_not_exist(self, primer):
        return (primer[self.length-2] == 'A' or primer[self.length-2] == 'T') or (primer[self.length-1] == 'A' or primer[self.length-1] == 'T')

    def multiple_occurrences_in_dna_sequence(self, dna_sequence, primer):
        return dna_sequence.count(primer) > 1

    def write_sequencing_primers_to_file(self, primers):
        if not os.path.isdir(self.directory_name):
            Path(os.path.join(self.directory_name)).mkdir()
        Path(os.path.join(self.directory_name, "sequencing_primers.csv")).touch()
        with open(os.path.join(self.directory_name, "sequencing_primers.csv"), 'w') as csvfile:
            csvfile.seek(0)
            csv.writer(csvfile, delimiter=',').writerow(primers)
