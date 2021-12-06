COMPLEMENTARY_NUCLEOTIDES = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


class DnaFragment:
    """A class representing a DNA fragment

    Attributes:
        name: Name of the DNA fragment as a string of characters
        sequence: Nucleotide sequence of the DNA fragment as a string of characters
    """

    def __init__(self, name=None, sequence=None):
        """Constructor of the class for creating a new DNA fragment

        Args:
            name: Name of the DNA fragment as a string of characters
            sequence: Nucleotide sequence of the DNA fragment as a string of characters
        """

        self.name = name
        self.sequence = sequence

    def get_name(self):
        """Returns the name of the DNA fragment

        Returns:
            DNA fragment name as a string of characters
        """

        return self.name

    def get_sequence(self):
        """Returns the nucleotide sequence of the DNA fragment

        Returns:
            DNA fragment nucleotide sequence as a string of characters
        """

        return self.sequence

    def get_reverse_complement(self):
        """Returns the reverse complement of the nucleotide sequence

        Returns:
            Reverse complement of the nucleotide sequence as a string of characters
        """

        if not self.sequence:
            return

        reverse_complement = ""
        for nucleotide in reversed(self.sequence):
            reverse_complement += COMPLEMENTARY_NUCLEOTIDES[nucleotide]
        return reverse_complement
