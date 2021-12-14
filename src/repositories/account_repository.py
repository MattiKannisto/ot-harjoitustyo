from entities.account import Account
from database_connection import get_connection_to_database


def get_account_row(row):
    """A method that returns an Account object based on a tuple obtained from the database

    Args:
        row: A tuple containing the account information
    Returns:
        An account object
    """

    return Account(row[0], row[1],
                   row[2], row[3],
                   row[4]) if row else None


class AccountRepository:
    """A class for carrying out account-related database operations
    """

    def __init__(self, connection_to_database):
        """Constructor of the class

        Args:
            connection_to_database: An object for creating a connection to the database        
        """

        self.connection_to_database = connection_to_database
        self.cursor = self.connection_to_database.cursor()

    def create(self, username, password, directory):
        """A method for creating a new account and storing it to the database

        Args:
            username: Username of the account as a string of characters
            password: Password of the account as a string of characters
            directory: Directory where output files will be stored as a string of characters
        """

        account = Account(username, password, directory)
        self.cursor.execute("insert into account (username, password, directory, sequencing_primer_length, sequencing_primer_gc_content) values (?, ?, ?, ?, ?)",
                            (account.username, account.password, account.directory, account.sequencing_primer_length, account.sequencing_primer_gc_content))
        self.connection_to_database.commit()

    def delete(self, account):
        """A method for deleting an account

        Args:
            account: Account to be deleted as an Account object
        """

        self.cursor.execute(
            "delete from account where username = ?", (account.username,))
        self.connection_to_database.commit()

    def find_by_name(self, username):
        """A method for getting an account from the database based on the username

        Args:
            username: Username of the account to be fetched from the database as a string of characters

        Returns:
            A user account as an Account object
        """

        self.cursor.execute(
            "select * from account where username = ?",
            (username,)
        )
        return get_account_row(self.cursor.fetchone())

    def update(self, account):
        """A method for updating a user account in the database

        Args:
            account: Account to be updated as an Account object
        """

        self.cursor.execute("update account set username = ?, password = ?, directory = ?, sequencing_primer_length = ?, sequencing_primer_gc_content = ? where username = ?",
                            (account.username, account.password, account.directory, account.sequencing_primer_length, account.sequencing_primer_gc_content, account.username))
        self.connection_to_database.commit()


account_repository = AccountRepository(get_connection_to_database())
