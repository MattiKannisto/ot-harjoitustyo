from entities.primer import Primer
from database_connection import get_connection_to_database


def generate_list_of_primers_from_rows(rows):
    """A method that returns a list of Primer objects based on a list of tuples obtained from the database

    Args:
        rows: A list of tuples containing the primer information

    Returns:
        primers: A list of Primer objects
    """

    primers = []
    for row in rows:
        primers.append(Primer(row[0], row[1], row[2]) if row else None)
    return primers


class PrimerRepository:
    """A class for carrying out database operations for primers
    """

    def __init__(self, connection_to_database):
        """Constructor of the class

        Args:
            connection_to_database: An object for creating a connection to the database
        """

        self.connection_to_database = connection_to_database
        self.cursor = self.connection_to_database.cursor()

    def create(self, name, sequence, template_dna_name):
        """Creates a new primer in the database

        Args:
            name: Name of the primer as a string of characters. Also a primary key of the table
            sequence: Nucleotide sequence of the primer as a string of characters
            template_dna_name: Name of the template DNA of the primer as a string of characters
        """

        self.cursor.execute("insert into primer (name, sequence, template_dna_name) values (?, ?, ?)",
                            (name, sequence, template_dna_name))
        self.connection_to_database.commit()

    def count_by_template_dna_name(self, template_dna_name):
        """Counts the rows from the table with a certain template_dna_name

        Args:
            template_dna_name: Name of the template dna as a string of characters
        Returns:
            The number of rows in the table with the template_dna_name value corresponding to the string given as a parameter
        """

        self.cursor.execute(
            "select count(*) from primer where template_dna_name = ?", (template_dna_name,))
        return self.cursor.fetchone()

    def find_all_by_template_dna_name(self, template_dna_name):
        """Fetches all rows from the table with a certain template_dna_name and returns a list of Primer objects

        Args:
            template_dna_name: Name of the template dna as a string of characters
        Returns:
            A list of Primer objects
        """

        self.cursor.execute(
            "select * from primer where template_dna_name = ?", (template_dna_name,))

        return generate_list_of_primers_from_rows(self.cursor.fetchall())


primer_repository = PrimerRepository(get_connection_to_database())
