class DnaFragment:
    """A class representing a DNA fragment

    Attributes:
        name: Name of the DNA fragment as a string of characters
        forward_strand: Forward strand of the nucleotide sequence of the DNA fragment as a string of characters
        reverse_strand: Reverse strand of the nucleotide sequence of the DNA fragment as a string of characters
        owner: Username of the account that has added this DNA fragment
    """

    def __init__(self, name, forward_strand, reverse_strand, owner):
        """Constructor of the class for creating a new DNA fragment

        Args:
            name: Name of the DNA fragment as a string of characters
            forward_strand: Forward strand of the nucleotide sequence of the DNA fragment as a string of characters
            reverse_strand: Reverse strand of the nucleotide sequence of the DNA fragment as a string of characters
            owner: Username of the account that has added this DNA fragment
        """

        self.name = name
        self.forward_strand = forward_strand
        self.reverse_strand = reverse_strand
        self.owner = owner
