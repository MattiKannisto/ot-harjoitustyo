ALLOWED_NUCLEOTIDES = ['A', 'T', 'G', 'C']

from entities.dna_fragment import DnaFragment
from repositories.dna_fragment_repository import dna_fragment_repository

class DnaFragmentService:
    def __init__(self):
        self.dna_fragment_repository = dna_fragment_repository

    def get_all_dna_fragments(self):
        return self.dna_fragment_repository.find_all()

    def get_dna_fragment_by_name(self, name):
        dna_fragment_as_tuple = self.dna_fragment_repository.find_by_name(name)
        return DnaFragment(dna_fragment_as_tuple[0], dna_fragment_as_tuple[1])

    def try_to_create_new_dna_fragment_and_return_notification(self, name, sequence):
        if name != "" and sequence != "":
            if self.dna_fragment_repository.find_by_name(name) != None:
                return ["You already have a DNA fragment with this name!", "red"]
            elif self.incorrect_letters_found(sequence):
                return ["Invalid DNA sequence! The sequence should contain only letters 'A', 'T', 'G' and 'C'", "red"]
            else:
                self.dna_fragment_repository.create(name, sequence)
                return ["DNA fragment '" + name + "' added", "green"]

    def incorrect_letters_found(self, sequence):
        """Checks if there letters in the nucleotide sequence that are not allowed

        Returns:
            A boolean True if the nucleotide sequence contains a letter that is not allowed
            A boolean False if the nucleotide sequence contains only allowed letters
        """

        if not sequence:
            return

        for nucleotide in sequence:
            if nucleotide not in ALLOWED_NUCLEOTIDES:
                return True
        return False
