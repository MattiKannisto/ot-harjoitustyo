class DnaFragment:
    """A class representing a DNA fragment

    Attributes:
        name: Name of the DNA fragment as a string
        for_strand: Forward strand of the nucleotide sequence of the DNA fragment as a string
        rev_strand: Reverse strand of the nucleotide sequence of the DNA fragment as a string
        owner_name: Name of the account that has added this DNA fragment
    """

    def __init__(self, name, for_strand, rev_strand, owner_name):
        """Constructor of the class for creating a new DNA fragment

        Args:
            name: Name of the DNA fragment as a string
            for_strand: Forward strand of the nucleotide sequence of the DNA fragment as a string
            rev_strand: Reverse strand of the nucleotide sequence of the DNA fragment as a string
            owner_name: Name of the account that has added this DNA fragment
        """

        self.name = name
        self.for_strand = for_strand
        self.rev_strand = rev_strand
        self.owner_name = owner_name
