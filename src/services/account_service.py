from repositories.account_repository import account_repository


class AccountService:
    """A class responsible for application logic related to accounts
    """

    def __init__(self):
        """A constructor for making a new AccountService object
        """

        self.account_repository = account_repository

    def get_account_by_name(self, name):
        """A method for getting an account from the database based on its name

        Args:
            name: Name of the account as a string of characters

        Returns:
            An Account object
        """

        return self.account_repository.find_by_name(name)

    def username_already_in_use(self, username):
        """A method for checking if the database contains an account with certain username

        Args:
            username: Username of the account to be searched from the database as a string of characters

        Returns:
            A Boolean False if an account with the given username could not be found in the database
            A boolean True if an account with the given username could be found in the database
        """

        return self.account_repository.find_by_name(username) is not None

    def create_account(self, username, password, directory):
        """A method for creating an account in the database

        Args:
            username: Username of the account to be created as a string of characters
            password: Password of the account to be created as a string of characters
            directory: Directory for output files of the account to be created as a string of characters
        """

        self.account_repository.create(username, password, directory)

    def delete_account(self, account):
        """A method for deleting an account

        Args:
            account: The account as an Account object
        """

        self.account_repository.delete(account)

    def update_account(self, account):
        """A method for updating an account based on an Account object

        Args:
            account: The account as an Account object
        """

        self.account_repository.update(account)
