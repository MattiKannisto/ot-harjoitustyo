class Primer:
    """A class representing a primer

    Attributes:
        name: Name of the primer as a string
        sequence: Nucleotide sequence of the primer as a string
        template_dna_name: Name of the template DNA fragment of the primer as string
    """

    def __init__(self, name, sequence, template_dna_name):
        """Constructor of the class for creating a new primer

        Args:
            name: Name of the primer as a string
            sequence: Nucleotide sequence of the primer as a string
            template_dna_name: Name of the template DNA fragment of the primer as string
        """

        self.name = name
        self.sequence = sequence
        self.template_dna_name = template_dna_name
