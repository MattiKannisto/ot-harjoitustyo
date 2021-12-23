class Account:
    """A class representing a user account

    Attributes:
        name: name of the account as a string
        password: Password of the account as a string
        directory: Directory of the account, where all output files will be saved, as a string
        primer_length: Length of the sequencing primer. Default value 20
        primer_gc_content: GC content of the sequencing primer. Default value of 0.5
    """

    def __init__(self, name, password, directory, primer_length=20, primer_gc_content=0.5):
        """Constructor of the class for creating a user account

        Args:
            name: name of the account as a string
            password: Password of the account as a string
            directory: Directory of the account, where all output files will be saved, as a string
            primer_length: Length of the sequencing primer. Default value 20
            primer_gc_content: GC content of the sequencing primer. Default value of 0.5
        """

        self.name = name
        self.password = password
        self.directory = directory
        self.primer_length = primer_length
        self.primer_gc_content = primer_gc_content
