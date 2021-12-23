from entities.account import Account
from repositories.account_repository import account_repository


class AccountService:
    """A class responsible for application logic related to accounts
    """

    def __init__(self, repository=account_repository):
        """A constructor for making a new AccountService object
        """

        self.logged_in_user = None
        self.creating_new_account = False
        self.changing_settings = False
        self.account_repository = repository

    def login(self, name, password):
        """A method for fetching account information as an Account object
           from the database based on name and account

        Args:
            name: name of the account to be fetched as a string
            password: password of the account to be fetched as a string
        """
        account_as_tuple = self.account_repository.find_by_name_and_password(
            name, password)
        self.logged_in_user = self._account_tuple_into_account_object(
            account_as_tuple)

    def logout(self):
        """A method for logging out the logged in account by setting it to None
        """
        self.logged_in_user = None

    def _account_tuple_into_account_object(self, account_tuple):
        if account_tuple:
            return Account(account_tuple[0], account_tuple[1],
                           account_tuple[2], account_tuple[3], account_tuple[4])
        return None

    def get_account_by_name(self, name):
        """A method for getting an account from the database based on its name

        Args:
            name: Name of the account as a string

        Returns:
            An Account object
        """
        account_as_tuple = self.account_repository.find_by_name(name)
        return self._account_tuple_into_account_object(account_as_tuple)

    def name_already_in_use(self, name):
        """A method for checking if the database contains an account with certain name

        Args:
            name: name of the account to be searched from the database as a string

        Returns:
            A boolean False if an account with the given name could not be found in the database
            A boolean True if an account with the given name could be found in the database
        """

        return self.account_repository.find_by_name(name) is not None

    def directory_already_in_use(self, directory):
        """A method for checking if the database contains an account with certain directory

        Args:
            directory: Directory of the account to be searched from the database as a string

        Returns:
            A boolean False if an account with the given directory could not be found in database
            A boolean True if an account with the given directory could be found in the database
        """

        return self.account_repository.find_by_directory(directory) is not None

    def create_account(self, name, password, re_typed_password, directory, notifications):
        """A method for creating an account in the database or returning a list of notifications
           indicating the reason why this was not done

        Args:
            name: name of the account to be created as a string
            password: Password of the account to be created as a string
            re_typed_password: Re-typed password of the account to be created as a string
            directory: Directory for output files of the account to be created as a string
            notifications: A list of two element string lists where first element is the
                           notification text and the second is notification color
        Returns:
            notifications: A list of notifications
        """

        if self.directory_already_in_use(directory):
            notifications.append(
                ["Someone else is already using this directory!", "red"])
        if not directory:
            notifications.append(
                ["You have not selected a working directory!", "red"])
        if password != re_typed_password:
            notifications.append(["Passwords do not match!", "red"])
        if self.name_already_in_use(name):
            notifications.append(["This name is already taken!", "red"])
        if len(name) < 5:
            notifications.append(
                ["name cannot be less than 5 characters!", "red"])
        if len(password) < 10:
            notifications.append(
                ["Password cannot be less than 10 characters!", "red"])
        if len(password) > 30:
            notifications.append(
                ["Password cannot be more than 30 characters!", "red"])
        if not notifications:
            account = Account(name, password, directory)
            self.account_repository.create(account.name, account.password, account.directory,
                                           account.primer_length, account.primer_gc_content)
            self.creating_new_account = False
        return notifications

    def delete_account(self):
        """A method for deleting logged in user's account
        """

        self.account_repository.delete(self.logged_in_user.name)
        self.logged_in_user = None

    def update_account(self):
        """A method for updating logged in user's account
        """

        self.account_repository.update(self.logged_in_user.name, self.logged_in_user.password,
                                       self.logged_in_user.directory,
                                       self.logged_in_user.primer_length,
                                       self.logged_in_user.primer_gc_content)
