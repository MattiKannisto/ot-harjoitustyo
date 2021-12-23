import os
from pathlib import Path
from openpyxl import Workbook
from entities.primer import Primer
from repositories.primer_repository import primer_repository

GC = ['G', 'C']

class PrimerService:
    def __init__(self, directory, primer_length, primer_gc_content):
        self.primer_repository = primer_repository
        self.directory = directory + "/primers"
        self.length = primer_length
        self.gc_content = primer_gc_content

    def _primer_tuples_into_primer_objects(self, rows):
        if rows:
            primers = []
            for row in rows:
                primers.append(Primer(row[0], row[1], row[2]))
            return primers
        return None

    def _generate_primers(self, dna_fragment):
        self._generate_primers_for_dna_strand(dna_fragment.name, "_for_", dna_fragment.for_strand)
        self._generate_primers_for_dna_strand(dna_fragment.name, "_rev_", dna_fragment.rev_strand)
        self._write_to_file(dna_fragment.name)

    def _generate_primers_for_dna_strand(self, name_prefix, name_infix, sequence):
        primers_added = int(self.primer_repository.count_by_name_prefix_and_infix(
            name_prefix + name_infix))
        for letter_index in range(len(sequence)-(self.length-1)):
            primer = sequence[letter_index:(letter_index + self.length)]
            if self._gc_content_incorrect(primer) or self._no_gc_lock(primer
               ) or self._multiple_occurrences(sequence, primer):
                continue
            if self.primer_repository.find_by_sequence_and_template_dna_name(primer,
                                                                             name_prefix) is None:
                self.primer_repository.create(name_prefix + name_infix + str(
                    primers_added+1), primer, name_prefix)
                primers_added += 1

    def _gc_content_incorrect(self, primer):
        return (primer.count('G') + primer.count('C')) != self.length * self.gc_content

    def _no_gc_lock(self, primer):
        return primer[-2] and primer[-1] not in GC

    def _multiple_occurrences(self, dna_sequence, primer):
        return dna_sequence.count(primer) > 1

    def attempt_primer_generation_and_return_notification(self, dna_fragment):
        """A method for attempting to generate sequencing primers, writing them to file
           and returning a notification on the failure or successfulness of this action

        Args:

        Returns:
            An array of two strings containing a notification text and a color of
            the notification if the DNA fragment's sequence is not None
        """

        if dna_fragment.for_strand:
            if len(dna_fragment.for_strand) < self.length:
                return ["DNA fragment shorter than primer length! Do you really want"
                        + "to sequence this DNA fragment?", "red"]
            count_before = self.primer_repository.count_by_template_dna_name(dna_fragment.name)
            self._generate_primers(dna_fragment)
            count_after = self.primer_repository.count_by_template_dna_name(dna_fragment.name)
            if count_after > count_before:
                return ["Sequencing primer file added to the directory '"
                        + self.directory + "'", "green"]
            return ["New primers were not found. Change settings and try again!", "yellow"]
        return ["Forward strand not specified for the DNA fragment!", "red"]

    def _write_to_file(self, dna_fragment_name):
        if not os.path.isdir(self.directory):
            Path(os.path.join(self.directory)).mkdir()
        file_name = self.directory + "/" + \
            dna_fragment_name + "_primers.xlsx"
        workbook = Workbook()
        active_sheet = workbook.active
        primer_tuples = self.primer_repository.find_all_by_template_dna_name(dna_fragment_name)
        primers = self._primer_tuples_into_primer_objects(primer_tuples)
        if primers:
            for primer in primers:
                active_sheet.append([primer.name, primer.sequence])
            workbook.save(file_name)
