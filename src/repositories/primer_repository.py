from database_connection import get_connection_to_database


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

    def count_by_name_prefix_and_infix(self, prefix_and_infix):
        """Counts the rows from the table with a certain prefix (same as template DNA name) and infix (_for or _rev)

        Args:
            prefix_and_infix: Primer name prefix and infix as a string of characters
        Returns:
            The number of rows in the table with the template_dna_name value corresponding to the string given as a parameter
        """

        self.cursor.execute(
            "select count(*) from primer where name like ?", ('%' + prefix_and_infix + '%',))
        return self.cursor.fetchone()[0]

    def count_by_template_dna_name(self, template_dna_name):
        """Counts the rows from the table with a certain template DNA name

        Args:
            template_dna_name: Name of the template DNA as a string of characters
        Returns:
            The number of rows in the table with the template_dna_name value corresponding to the string given as a parameter
        """

        self.cursor.execute(
            "select count(*) from primer where template_dna_name = ?", (template_dna_name,))
        return self.cursor.fetchone()[0]

    def find_by_sequence_and_template_dna_name(self, sequence, template_dna_name):
        """Fetches a primer tuple from the database based on the sequence and template DNA name

        Args:
            sequence: Nucleotide sequence of the primer to be fetched from the database
            template_dna_name: Name of the template DNA as a string of characters
        """

        self.cursor.execute(
            "select * from primer where sequence = ? and template_dna_name = ?", (sequence, template_dna_name,))

        return self.cursor.fetchone()


    def find_all_by_template_dna_name(self, template_dna_name):
        """Fetches all rows from the table with a certain template_dna_name and returns a list of tuples in descending order of primer name

        Args:
            template_dna_name: Name of the template dna as a string of characters
        Returns:
            A list of tuples containing the primer information
        """

        self.cursor.execute(
            "select * from primer where template_dna_name = ?", (template_dna_name,))

        return self.cursor.fetchall()


primer_repository = PrimerRepository(get_connection_to_database())
