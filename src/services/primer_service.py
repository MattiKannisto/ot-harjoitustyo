import os
from pathlib import Path
from openpyxl import Workbook
from repositories.primer_repository import primer_repository


class PrimerService:
    def __init__(self, directory, sequencing_primer_length, sequencing_primer_gc_content):
        self.sequencing_primer_repository = primer_repository
        self.directory = directory + "/primers"
        self.length = sequencing_primer_length
        self.gc_content = sequencing_primer_gc_content

    def generate_sequencing_primers(self, dna_fragment):
        self.generate_sequencing_primers_for_dna_strand(
            dna_fragment.name, "_for_", dna_fragment.sequence)
        self.generate_sequencing_primers_for_dna_strand(
            dna_fragment.name, "_rev_", dna_fragment.get_reverse_complement())
        self.write_sequencing_primers_to_file(
            dna_fragment.name)

    def generate_sequencing_primers_for_dna_strand(self, dna_fragment_name, name_infix, dna_sequence):
        primers_added = 0
        for letter_index in range(len(dna_sequence)-(self.length-1)):
            sequencing_primer_candidate = dna_sequence[letter_index:(
                letter_index + self.length)]
            if self.gc_content_is_incorrect(sequencing_primer_candidate) or self.gc_lock_does_not_exist(sequencing_primer_candidate) or self.multiple_occurrences_in_dna_sequence(dna_sequence, sequencing_primer_candidate):
                continue
            self.sequencing_primer_repository.create(dna_fragment_name + name_infix + str(
                primers_added+1), sequencing_primer_candidate, dna_fragment_name)
            primers_added += 1

    def gc_content_is_incorrect(self, primer):
        return (primer.count('G') + primer.count('C')) != self.length * self.gc_content

    def gc_lock_does_not_exist(self, primer):
        return (primer[self.length-2] == 'A' or primer[self.length-2] == 'T') or (primer[self.length-1] == 'A' or primer[self.length-1] == 'T')

    def multiple_occurrences_in_dna_sequence(self, dna_sequence, primer):
        return dna_sequence.count(primer) > 1

    def attempt_primer_generation_and_return_notification(self, dna_fragment):
        if dna_fragment.sequence:
            self.generate_sequencing_primers(dna_fragment)
            return ["Sequencing primer file added to the directory '" + self.directory + "'", "blue"]

    def write_sequencing_primers_to_file(self, dna_fragment_name):
        if not os.path.isdir(self.directory):
            Path(os.path.join(self.directory)).mkdir()
        file_name = self.directory + "/" + \
            dna_fragment_name + "_sequencing_primers.xlsx"
        workbook = Workbook()
        active_sheet = workbook.active
        primers = self.sequencing_primer_repository.find_all_by_template_dna_name(
            dna_fragment_name)
        for primer in primers:
            active_sheet.append([primer.name, primer.sequence])
        workbook.save(file_name)
