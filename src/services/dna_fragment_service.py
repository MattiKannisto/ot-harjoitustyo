from entities.dna_fragment import DnaFragment
from repositories.dna_fragment_repository import dna_fragment_repository
ALLOWED_NUCLEOTIDES = ['A', 'T', 'G', 'C']
COMPLEMENTARY_NUCLEOTIDES = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


class DnaFragmentService:
    def __init__(self, repository=dna_fragment_repository):
        """A class responsible for DNA fragment related application logic
        """

        self.dna_fragment_repository = repository

    def _dna_fragment_tuple_into_dna_fragment_object(self, tuple):
        if tuple:
            return DnaFragment(tuple[0], tuple[1], tuple[2], tuple[3])

    def get_all_dna_fragments_by_owner(self, owner):
        """A method for getting all DNA fragments from the database based on DNA fragment owner

        Args:
            owner: Username of the owner of the DNA fragment to be fetched as a string of characters

        Returns:
            A list of tuples containing the information about all DNA fragments of the owner Account in the database
        """

        return self.dna_fragment_repository.find_all_by_owner(owner)

    def get_dna_fragment_by_name_and_owner(self, name, owner):
        """A method for getting a DNA fragment from the database based on its name and owner

        Args:
            name: Name of the DNA fragment as a string of characters
            owner: Username of the account that has added the DNA fragment to the database

        Returns:
            The DNA fragment as a DnaFragment object
        """
        dna_fragment_tuple = self.dna_fragment_repository.find_by_name_and_owner(name, owner)
        return self._dna_fragment_tuple_into_dna_fragment_object(dna_fragment_tuple)

    def try_to_create_new_dna_fragment_and_return_notification(self, name, sequence, owner):
        """A method for attempting addition of a new DNA fragment into the database and returning a notification on the failure or successfulness of this action

        Args:
            name: Name of the DNA fragment to be saved into the database
            sequence: Nucleotide sequence of the DNA fragment to be saved into the database

        Returns:
            A two element array of stings of characters containing the notification and a color in which the notification will be displayed in
        """

        if self.dna_fragment_repository.find_by_name_and_owner(name, owner) != None:
            return ["You already have a DNA fragment with this name!", "red"]
        elif self._incorrect_letters_found(sequence):
            return ["Invalid DNA sequence! The sequence should contain only letters 'A', 'T', 'G' and 'C'", "red"]
        else:
            self.dna_fragment_repository.create(name, sequence, self._get_reverse_complement(sequence), owner)
            return ["DNA fragment '" + name + "' added", "green"]

    def _incorrect_letters_found(self, sequence):
        for nucleotide in sequence:
            if nucleotide not in ALLOWED_NUCLEOTIDES:
                return True
        return False

    def _get_reverse_complement(self, sequence):
        reverse_complement = ""
        for nucleotide in reversed(sequence):
            reverse_complement += COMPLEMENTARY_NUCLEOTIDES[nucleotide]
        return reverse_complement