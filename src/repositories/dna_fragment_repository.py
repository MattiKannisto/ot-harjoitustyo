from database_connection import get_connection_to_database


class DnaFragmentRepository:
    """A class for carrying out DNA fragment related database operations
    """

    def __init__(self, connection_to_database):
        """Constructor of the class

        Args:
            connection_to_database: An object for creating a connection to the database        
        """

        self.connection_to_database = connection_to_database
        self.cursor = self.connection_to_database.cursor()

    def create(self, name, forward_strand, reverse_strand, owner):
        """A method for creating a new DnaFragment object and storing it in the database

        Args:
            name: Name of the DNA fragment to be added to the database as a string of characters
            forward_strand: Forward strand of the nucleotide sequence of the DNA fragment to be added to the database as a string of characters
            reverse_strand: Reverse strand of the nucleotide sequence of the DNA fragment to be added to the database as a string of characters
            owner: Username of the account that has added the DNA fragment as a string of characters
        """

        self.cursor.execute("insert into dna_fragment (name, forward_strand, reverse_strand, owner) values (?, ?, ?, ?)",
                            (name, forward_strand, reverse_strand, owner))
        self.connection_to_database.commit()

    def find_by_name_and_owner(self, name, owner):
        """A method for getting a DNA fragment from the database based on its name and owner username

        Args:
            name: Name of the DNA fragment to be fetched from the database as a string of characters
            owner: Username of the account that has added the DNA fragment to be fetched from the database as a string of characters

        Returns:
            The DNA fragment as a tuple
        """

        self.cursor.execute(
            'select * from dna_fragment where name = ? and owner = ?',
            (str(name), str(owner),)
        )
        return self.cursor.fetchone()

    def find_all_by_owner(self, owner):
        """A method for getting all DnaFragments from the database based on the owner username

        Args:
            owner: Username of the account that has added the DNA fragment to be fetched from the database as a string of characters

        Returns:
            A list of tuples
        """

        self.cursor.execute("select * from dna_fragment where owner = ?", (owner,))
        return list(self.cursor.fetchall())


dna_fragment_repository = DnaFragmentRepository(get_connection_to_database())
