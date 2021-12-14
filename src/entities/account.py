class Account:
    """A class representing a user account

    Attributes:
        username: Username of the account as a string of characters
        password: Password of the account as a string of characters
        directory: Directory of the account, where all output files will be saved, as a string of characters
        sequencing_primer_length: Length of the sequencing primer. Set to default value of 20 when a new user account is created but can be changed by the user later
        sequencing_primer_gc_content: GC content of the sequencing primer. Set to default value of 0.5 when a new user account is created but can be changed by the user later
    """

    def __init__(self, username, password, directory, sequencing_primer_length=20, sequencing_primer_gc_content=0.5):
        """Constructor of the class for creating a user account

        Args:
            username: Username of the account as a string of characters
            password: Password of the account as a string of characters
            directory: Directory of the account, where all output files will be saved, as a string of characters
            sequencing_primer_length: Length of the sequencing primer. Set to default value of 20 when a new user account is created but can be changed by the user later
            sequencing_primer_gc_content: GC content of the sequencing primer. Set to default value of 0.5 when a new user account is created but can be changed by the user later
        """

        self.username = username
        self.password = password
        self.directory = directory
        self.sequencing_primer_length = sequencing_primer_length
        self.sequencing_primer_gc_content = sequencing_primer_gc_content
