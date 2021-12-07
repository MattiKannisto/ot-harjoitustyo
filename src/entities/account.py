class Account:
    """A class representing a user account

    Attributes:
        username: Username of the account as a string of characters
        password: Password of the account as a string of characters
        directory: Directory of the account, where all output files will be saved, as a string of characters
    """

    def __init__(self, username, password, directory):
        """Constructor of the class for creating a user account

        Args:
            username: Username of the account as a string of characters
            password: Password of the account as a string of characters
            directory: Directory of the account, where all output files will be saved, as a string of characters
        """

        self.username = username
        self.password = password
        self.directory = directory
