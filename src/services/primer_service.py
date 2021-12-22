import os
from pathlib import Path
from openpyxl import Workbook
from entities.primer import Primer
from repositories.primer_repository import primer_repository


class PrimerService:
    def __init__(self, directory, sequencing_primer_length, sequencing_primer_gc_content):
        self.sequencing_primer_repository = primer_repository
        self.directory = directory + "/primers"
        self.length = sequencing_primer_length
        self.gc_content = sequencing_primer_gc_content

    def _primer_tuples_into_primer_objects(self, rows):
        if rows:
            primers = []
            for row in rows:
                primers.append(Primer(row[0], row[1], row[2]))
            return primers
        
    def _generate_sequencing_primers(self, dna_fragment):
        self._generate_sequencing_primers_for_dna_strand(
            dna_fragment.name, "_for_", dna_fragment.forward_strand)
        self._generate_sequencing_primers_for_dna_strand(
            dna_fragment.name, "_rev_", dna_fragment.reverse_strand)
        self._write_sequencing_primers_to_file(
            dna_fragment.name)

    def _generate_sequencing_primers_for_dna_strand(self, dna_fragment_name, name_infix, dna_sequence):
        primers_added = int(self.sequencing_primer_repository.count_by_name_prefix_and_infix(dna_fragment_name + name_infix))
        for letter_index in range(len(dna_sequence)-(self.length-1)):
            sequencing_primer_candidate = dna_sequence[letter_index:(
                letter_index + self.length)]
            if self._gc_content_is_incorrect(sequencing_primer_candidate) or self._gc_lock_does_not_exist(sequencing_primer_candidate) or self._multiple_occurrences_in_dna_sequence(dna_sequence, sequencing_primer_candidate):
                continue
            if self.sequencing_primer_repository.find_by_sequence_and_template_dna_name(sequencing_primer_candidate, dna_fragment_name) == None:
                self.sequencing_primer_repository.create(dna_fragment_name + name_infix + str(
                    primers_added+1), sequencing_primer_candidate, dna_fragment_name)
                primers_added += 1

    def _gc_content_is_incorrect(self, primer):
        return (primer.count('G') + primer.count('C')) != self.length * self.gc_content

    def _gc_lock_does_not_exist(self, primer):
        return (primer[self.length-2] == 'A' or primer[self.length-2] == 'T') or (primer[self.length-1] == 'A' or primer[self.length-1] == 'T')

    def _multiple_occurrences_in_dna_sequence(self, dna_sequence, primer):
        return dna_sequence.count(primer) > 1

    def attempt_primer_generation_and_return_notification(self, dna_fragment):
        """A method for attempting to generate sequencing primers, writing them to file and returning a notification on the failure or successfulness of this action

        Args:

        Returns:
            An array of two strings of characters containing a notification text and a color of the notification if the DNA fragment's sequence is not None
        """

        if dna_fragment.forward_strand:
            if len(dna_fragment.forward_strand) < self.length:
                return ["DNA fragment shorter than primer length! Do you really want to sequence this DNA fragment?", "red"]
            count_before = self.sequencing_primer_repository.count_by_template_dna_name(dna_fragment.name)
            self._generate_sequencing_primers(dna_fragment)
            count_after = self.sequencing_primer_repository.count_by_template_dna_name(dna_fragment.name)
            if count_after > count_before:
                return ["Sequencing primer file added to the directory '" + self.directory + "'", "green"]
            else:
                return ["New primers were not found. Change settings and try again!", "yellow"]

    def _write_sequencing_primers_to_file(self, dna_fragment_name):
        if not os.path.isdir(self.directory):
            Path(os.path.join(self.directory)).mkdir()
        file_name = self.directory + "/" + \
            dna_fragment_name + "_sequencing_primers.xlsx"
        workbook = Workbook()
        active_sheet = workbook.active
        primers = self._primer_tuples_into_primer_objects(self.sequencing_primer_repository.find_all_by_template_dna_name(
            dna_fragment_name))
        if primers:
            for primer in primers:
                active_sheet.append([primer.name, primer.sequence])
            workbook.save(file_name)
