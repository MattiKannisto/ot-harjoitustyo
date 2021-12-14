from entities.dna_fragment import DnaFragment
from database_connection import get_connection_to_database


def get_dna_fragment_row(row):
    """A method that returns a DnaFragment object based on a tuple containing information about the DNA fragment

    Args:
        row: A tuple containing the DNA fragment information from the database

    Returns:
        A DnaFragment object
    """

    return DnaFragment(row[0], row[1]) if row else None


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

    def create(self, name, sequence):
        """A method for creating a new DnaFragment object and storing it in the database

        Args:
            name: Name of the DNA fragment to be added to the database as a string of characters
            sequence: Nucleotide sequence of the DNA fragment to be added to the database as a string of characters
        """

        self.cursor.execute("insert into dna_fragment (name, sequence) values (?, ?)",
                            (name, sequence))
        self.connection_to_database.commit()

    def find_by_name(self, name):
        """A method for getting a DNA fragment from the database based on its name

        Args:
            name: Name of the DNA fragment to be fetched from the database as a string of characters

        Returns:
            A DnaFragment object
        """

        self.cursor.execute(
            'select * from dna_fragment where name = ?',
            (name,)
        )
        return get_dna_fragment_row(self.cursor.fetchone())

    def find_all(self):
        """A method for getting all DnaFragments from the database

        Returns:
            A list of tuples
        """

        self.cursor.execute("select * from dna_fragment")
        return list(self.cursor.fetchall())


dna_fragment_repository = DnaFragmentRepository(get_connection_to_database())
