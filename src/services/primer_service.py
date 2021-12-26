import os
from pathlib import Path
from openpyxl import Workbook
from entities.primer import Primer
from repositories.primer_repository import primer_repository

GC = ['G', 'C']


class PrimerService:
    """A class responsible for primer related application logic
    """

    def __init__(self, repository=primer_repository):
        """A constructor for making a new PrimerService object

        Args:
            repository: A repository object
        """

        self._primer_repository = repository

    def _tuples_into_objects(self, primer_tuples):
        if primer_tuples:
            primers = []
            for primer_tuple in primer_tuples:
                primers.append(Primer(primer_tuple[0], primer_tuple[1], primer_tuple[2]))
            return primers
        return None

    def _generate_primers(self, length, gc_content, name_prefix, name_infix, sequence):
        primers_added = int(self._primer_repository.count_by_name_prefix_and_infix(
            name_prefix + name_infix))
        for letter_index in range(len(sequence)-(length-1)):
            primer = sequence[letter_index:(letter_index + length)]
            if self._gc_content_incorrect(gc_content, primer
                                          ) or self._no_gc_lock(
                    primer) or self._multiple_occurrences(sequence, primer):
                continue
            if self._primer_repository.find_by_sequence_and_template_dna_name(primer,
                                                                              name_prefix) is None:
                self._primer_repository.create(name_prefix + name_infix + str(
                    primers_added+1), primer, name_prefix)
                primers_added += 1

    def _gc_content_incorrect(self, gc_content, primer):
        return float((primer.count('G') + primer.count('C'))/len(primer)) != gc_content

    def _no_gc_lock(self, primer):
        return (primer[-2] not in GC) or (primer[-1] not in GC)

    def _multiple_occurrences(self, dna_sequence, primer):
        return dna_sequence.count(primer) > 1

    def attempt_primer_generation_and_return_notification(self, directory, length,
                                                          gc_content, dna_fragment_name,
                                                          for_strand, rev_strand):
        """A method for attempting to generate sequencing primers, writing them to file
           and returning a notification on the failure or successfulness of this action

        Args:
            directory: Directory of the logged in account as string
            length: Length of the primers of the logged in account
            gc_content: GC content of the primers of the logged in account
            dna_fragment_name: Name of the template DNA fragment as string
            for_strand: Forward strand of the template DNA as string
            rev_strand: Reverse strand of the template DNA as string

        Returns:
            An array of two strings containing a notification text and a color of
            the notification if the DNA fragment's forward strand is not None
        """

        if for_strand:
            if len(for_strand) < length:
                return ["DNA fragment shorter than primer length! Do you really want"
                        + "to sequence this DNA fragment?", "red"]
            count_before = self._primer_repository.count_by_template_dna_name(dna_fragment_name)
            self._generate_primers(length, gc_content, dna_fragment_name, "_for_", for_strand)
            self._generate_primers(length, gc_content, dna_fragment_name, "_rev_", rev_strand)
            self._write_to_file(directory, dna_fragment_name)
            count_after = self._primer_repository.count_by_template_dna_name(dna_fragment_name)
            if count_after > count_before:
                return ["Sequencing primer file added to the directory '"+ directory +"'", "green"]
            return ["New primers were not found. Change settings and try again!", "yellow"]
        return ["Forward strand not specified for the DNA fragment!", "red"]

    def delete_all_by_template_dna_name(self, template_dna_name):
        """Deletes all primers from database based on template DNA name

        Args:
            name: Name of the template DNA
        """
        self._primer_repository.delete_by_template_dna_name(template_dna_name)

    def _write_to_file(self, directory, dna_fragment_name):
        directory = directory + "/primers"
        if not os.path.isdir(directory):
            Path(os.path.join(directory)).mkdir()
        file_name = directory + "/" + \
            dna_fragment_name + "_primers.xlsx"
        workbook = Workbook()
        active_sheet = workbook.active
        primer_tuples = self._primer_repository.find_all_by_template_dna_name(dna_fragment_name)
        primers = self._tuples_into_objects(primer_tuples)
        if primers:
            for primer in primers:
                active_sheet.append([primer.name, primer.sequence])
            workbook.save(file_name)
