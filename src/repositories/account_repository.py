from database_connection import get_connection_to_database


class AccountRepository:
    """A class for carrying out account-related database operations
    """

    def __init__(self, connection_to_database):
        """Constructor of the class

        Args:
            connection_to_database: An object for creating a connection to the database        
        """

        self._connection_to_database = connection_to_database
        self._cursor = self._connection_to_database.cursor()

    def create(self, name, password, directory, primer_length, primer_gc_content):
        """A method for creating a new account and storing it to the database

        Args:
            name: name of the account as a string
            password: Password of the account as a string
            directory: Directory where output files will be stored as a string
            primer_length: Length of the sequencing primers that will be generated as an integer
            primer_gc_content = GC content of the sequencing primers that will be generated as a float
        """

        self._cursor.execute("insert into account (name, password, directory, "
                             + "primer_length, primer_gc_content) values (?, ?, ?, ?, ?)",
                             (str(name), str(password), str(directory),
                              int(primer_length), float(primer_gc_content,)))
        self._connection_to_database.commit()

    def delete(self, name):
        """A method for deleting an account

        Args:
            name: name of the account to be deleted as a string
        """

        self._cursor.execute(
            "delete from account where name = ?", (name,))
        self._connection_to_database.commit()

    def find_by_name_and_password(self, name, password):
        """A method for getting an account from the database based on the name and password

        Args:
            name: name of the account to be fetched from the database as a string
            password: Password of the account to be fetched from the database as a string

        Returns:
            A user account as a tuple
        """

        self._cursor.execute(
            "select * from account where name = ? and password = ?",
            (name, password,)
        )
        return self._cursor.fetchone()

    def find_by_name(self, name):
        """A method for getting an account from the database based on the name

        Args:
            name: name of the account to be fetched from the database as a string

        Returns:
            A user account as a tuple
        """

        self._cursor.execute(
            "select * from account where name = ?",
            (name,)
        )
        return self._cursor.fetchone()

    def find_by_directory(self, directory):
        """A method for getting an account from the database based on the directory

        Args:
            directory: Directory of the account to be fetched as a string

        Returns:
            A user account as a tuple
        """

        self._cursor.execute(
            "select * from account where directory = ?",
            (str(directory),)
        )
        return self._cursor.fetchone()

    def update(self, name, password, directory, primer_length, primer_gc_content):
        """A method for updating a user account in the database

        Args:
            name: name of the account to be updated as a string
            password: Password of the account to be updated as a string
            directory: Directory of the account to be updated as a string
            primer_length: Length of the sequencing primers of the account to be updated as an integer
            primer_gc_content = GC content of the sequencing primers of the account to be updated as a float
        """

        self._cursor.execute("update account set name = ?, password = ?, directory = ?, primer_length = ?, primer_gc_content = ? where name = ?",
                             (str(name), str(password), str(directory), int(primer_length), float(primer_gc_content), str(name)))
        self._connection_to_database.commit()


account_repository = AccountRepository(get_connection_to_database())
