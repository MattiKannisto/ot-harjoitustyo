class Primer:
    """A class representing a primer

    Attributes:
        name: Name of the primer as a string of characters
        sequence: Nucleotide sequence of the primer as a string of characters
    """

    def __init__(self, name, sequence, template_dna_name):
        """Constructor of the class for creating a new primer

        Args:
            name: Name of the primer as a string of characters
            sequence: Nucleotide sequence of the primer as a string of characters
        """

        self.name = name
        self.sequence = sequence
        self.template = template_dna_name
