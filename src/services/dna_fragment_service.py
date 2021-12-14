from repositories.dna_fragment_repository import dna_fragment_repository
ALLOWED_NUCLEOTIDES = ['A', 'T', 'G', 'C']


class DnaFragmentService:
    def __init__(self):
        """A class responsible for DNA fragment related application logic
        """

        self.dna_fragment_repository = dna_fragment_repository

    def get_all_dna_fragments(self):
        """A method for getting all DNA fragments from the database

        Returns:
            A list of tuples containing the information about all DNA fragments in the database
        """

        return self.dna_fragment_repository.find_all()

    def get_dna_fragment_by_name(self, name):
        """A method for getting a DNA fragment from the database based on its name

        Args:
            name: Name of the DNA fragment as a string of characters

        Returns:
            The DNA fragment as a DnaFragment object
        """

        return self.dna_fragment_repository.find_by_name(name)

    def try_to_create_new_dna_fragment_and_return_notification(self, name, sequence):
        """A method for attempting addition of a new DNA fragment into the database and returning a notification on the failure or successfulness of this action

        Args:
            name: Name of the DNA fragment to be saved into the database
            sequence: Nucleotide sequence of the DNA fragment to be saved into the database

        Returns:
            A two element array of stings of characters containing the notification and a color in which the notification will be displayed in
        """

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
            None if the sequence given is ""
            A boolean True if the nucleotide sequence contains a letter that is not allowed
            A boolean False if the nucleotide sequence contains only allowed letters
        """

        if not sequence:
            return

        for nucleotide in sequence:
            if nucleotide not in ALLOWED_NUCLEOTIDES:
                return True
        return False
