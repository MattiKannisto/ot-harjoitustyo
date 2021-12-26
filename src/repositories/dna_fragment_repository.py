from database_connection import get_connection_to_database


class DnaFragmentRepository:
    """A class for carrying out DNA fragment related database operations
    """

    def __init__(self, connection_to_database):
        """Constructor of the class

        Args:
            connection_to_database: An object for creating a connection to the database
        """

        self._connection_to_database = connection_to_database
        self._cursor = self._connection_to_database.cursor()

    def create(self, name, for_strand, rev_strand, owner_name):
        """A method for creating a new DnaFragment object and storing it in the database

        Args:
            name: Name of the DNA fragment as a string
            for_strand: Forward strand of the DNA fragment as a string
            rev_strand: Reverse strand of the DNA fragment as a string
            owner_name: name of the account that has added the DNA fragment as a string
        """

        self._cursor.execute("insert into dna_fragment (name, for_strand, rev_strand, owner_name)"
                             + "values (?, ?, ?, ?)",
                             (name, for_strand, rev_strand, owner_name))
        self._connection_to_database.commit()

    def delete_by_name(self, name):
        """A method for deleting a new DnaFragment based on its name

        Args:
            name: Name of the DNA fragment as a string
        """

        self._cursor.execute(
            "delete from dna_fragment where name = ?", (name,))
        self._connection_to_database.commit()

    def find_by_name_and_owner_name(self, name, owner_name):
        """A method for getting a DNA fragment from the database based on its name and owner_name

        Args:
            name: Name of the DNA fragment to be fetched as a string
            owner_name: Name of the account that has added the DNA fragment to database

        Returns:
            The DNA fragment as a tuple
        """

        self._cursor.execute(
            'select * from dna_fragment where name = ? and owner_name = ?',
            (str(name), str(owner_name),)
        )
        return self._cursor.fetchone()

    def find_by_name(self, name):
        """A method for getting a DnaFragment from the database based on name

        Args:
            name: Name of the DNA fragment

        Returns:
            A tuple containing DNA fragment information
        """

        self._cursor.execute(
            "select * from dna_fragment where name = ?", (name,))
        return self._cursor.fetchone()

    def find_all_by_owner_name(self, owner_name):
        """A method for getting all DnaFragments from the database based on the owner name

        Args:
            owner_name: Name of the account that has added the DNA fragment to database

        Returns:
            A list of tuples
        """

        self._cursor.execute(
            "select * from dna_fragment where owner_name = ?", (owner_name,))
        return list(self._cursor.fetchall())


dna_fragment_repository = DnaFragmentRepository(get_connection_to_database())
