class Primer:
    """A class representing a primer

    Attributes:
        name: Name of the primer as a string of characters
        sequence: Nucleotide sequence of the primer as a string of characters
        template: Name of the template DNA fragment into which the primer anneals to
    """

    def __init__(self, name, sequence, template):
        """Constructor of the class for creating a new primer

        Args:
            name: Name of the primer as a string of characters
            sequence: Nucleotide sequence of the primer as a string of characters
            template: Name of the template DNA fragment into which the primer anneals to
        """

        self.name = name
        self.sequence = sequence
        self.template = template
