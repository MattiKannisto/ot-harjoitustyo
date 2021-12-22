from database_connection import get_connection_to_database


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

    def create(self, username, password, directory, sequencing_primer_length, sequencing_primer_gc_content):
        """A method for creating a new account and storing it to the database

        Args:
            username: Username of the account as a string of characters
            password: Password of the account as a string of characters
            directory: Directory where output files will be stored as a string of characters
            sequencing_primer_length: Length of the sequencing primers that will be generated as an integer
            sequencing_primer_gc_content = GC content of the sequencing primers that will be generated as a float
        """

        self.cursor.execute("insert into account (username, password, directory, sequencing_primer_length, sequencing_primer_gc_content) values (?, ?, ?, ?, ?)",
                            (str(username), str(password), str(directory), int(sequencing_primer_length), float(sequencing_primer_gc_content,)))
        self.connection_to_database.commit()

    def delete(self, username):
        """A method for deleting an account

        Args:
            username: Username of the account to be deleted as a string of characters
        """

        self.cursor.execute(
            "delete from account where username = ?", (username,))
        self.connection_to_database.commit()

    def find_by_name_and_password(self, username, password):
        """A method for getting an account from the database based on the username and password

        Args:
            username: Username of the account to be fetched from the database as a string of characters
            password: Password of the account to be fetched from the database as a string of characters

        Returns:
            A user account as a tuple
        """

        self.cursor.execute(
            "select * from account where username = ? and password = ?",
            (username, password,)
        )
        return self.cursor.fetchone()

    def find_by_name(self, username):
        """A method for getting an account from the database based on the username

        Args:
            username: Username of the account to be fetched from the database as a string of characters

        Returns:
            A user account as a tuple
        """

        self.cursor.execute(
            "select * from account where username = ?",
            (username,)
        )
        return self.cursor.fetchone()

    def find_by_directory(self, directory):
        """A method for getting an account from the database based on the directory

        Args:
            directory: Directory of the account to be fetched as a string of characters

        Returns:
            A user account as a tuple
        """

        self.cursor.execute(
            "select * from account where directory = ?",
            (str(directory),)
        )
        return self.cursor.fetchone()


    def update(self, username, password, directory, sequencing_primer_length, sequencing_primer_gc_content):
        """A method for updating a user account in the database

        Args:
            username: Username of the account to be updated as a string of characters
            password: Password of the account to be updated as a string of characters
            directory: Directory of the account to be updated as a string of characters
            sequencing_primer_length: Length of the sequencing primers of the account to be updated as an integer
            sequencing_primer_gc_content = GC content of the sequencing primers of the account to be updated as a float
        """

        self.cursor.execute("update account set username = ?, password = ?, directory = ?, sequencing_primer_length = ?, sequencing_primer_gc_content = ? where username = ?",
                            (str(username), str(password), str(directory), int(sequencing_primer_length), float(sequencing_primer_gc_content), str(username)))
        self.connection_to_database.commit()


account_repository = AccountRepository(get_connection_to_database())
