from entities.dna_fragment import DnaFragment
from repositories.dna_fragment_repository import dna_fragment_repository

ALLOWED_NUCLEOTIDES = ['A', 'T', 'G', 'C']
COMPLEMENTARY_NUCLEOTIDES = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


class DnaFragmentService:
    """A class responsible for DNA fragment related application logic
    """

    def __init__(self, repository=dna_fragment_repository):
        """A constructor for making a new DnaFragment object

        Args:
            repository: A repository object
        """


        self._dna_fragment_repository = repository

    def _tuple_into_object(self, dna_tuple):
        if dna_tuple:
            return DnaFragment(dna_tuple[0], dna_tuple[1], dna_tuple[2], dna_tuple[3])
        return None

    def get_all_dna_fragments_by_owner_name(self, owner_name):
        """A method for getting all DNA fragments from the database based on DNA fragment owner

        Args:
            owner_name: Username of the owner of the DNA fragment to be fetched as a string

        Returns:
            A list of tuples containing the information about all DNA fragments of the owner
        """

        return self._dna_fragment_repository.find_all_by_owner_name(owner_name)

    def get_dna_fragment_by_name_and_owner_name(self, name, owner_name):
        """A method for getting a DNA fragment from the database based on its name and owner

        Args:
            name: Name of the DNA fragment as a string
            owner_name: Username of the account that has added the DNA fragment to the database

        Returns:
            The DNA fragment as a DnaFragment object
        """
        dna_fragment_tuple = self._dna_fragment_repository.find_by_name_and_owner_name(
            name, owner_name)
        return self._tuple_into_object(dna_fragment_tuple)

    def try_to_create_new_dna_fragment_and_return_notification(self, name, sequence, owner_name):
        """A method for attempting addition of a new DNA fragment into the database and returning
           a notification on the failure or successfulness of this action

        Args:
            name: Name of the DNA fragment to be saved into the database
            sequence: Nucleotide sequence of the DNA fragment to be saved into the database
            owner_name: Name of the account adding the DNA fragment to database
        Returns:
            A two element array of strings containing the notification text and color
        """

        if self._dna_fragment_repository.find_by_name_and_owner_name(name, owner_name) is not None:
            return ["You already have a DNA fragment with this name!", "red"]
        if self._dna_fragment_repository.find_by_name(name) is not None:
            return ["A fragment with this name already exists, please try another name!", "red"]
        if self._incorrect_letters_found(sequence):
            return ["Invalid DNA sequence! The sequence should contain only letters "
                    + "'A', 'T', 'G' and 'C'", "red"]
        self._dna_fragment_repository.create(
            name, sequence, self._get_reverse_complement(sequence), owner_name)
        return ["DNA fragment '" + name + "' added", "green"]

    def delete_by_name(self, name):
        """Deletes a DNA fragment from database based on DNA fragment name

        Args:
            name: Name of the DNA fragment
        """
        self._dna_fragment_repository.delete_by_name(name)

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
