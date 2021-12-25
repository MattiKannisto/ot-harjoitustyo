from database_connection import get_connection_to_database


class PrimerRepository:
    """A class for carrying out database operations for primers
    """

    def __init__(self, connection_to_database):
        """Constructor of the class

        Args:
            connection_to_database: An object for creating a connection to the database
        """

        self._connection_to_database = connection_to_database
        self._cursor = self._connection_to_database.cursor()

    def create(self, name, sequence, template_dna_name):
        """Creates a new primer in the database

        Args:
            name: Name of the primer as a string
            sequence: Nucleotide sequence of the primer as a string
            template_dna_name: Name of the template DNA of the primer as a string
        """

        self._cursor.execute("insert into primer (name, sequence, template_dna_name) "
                             + "values (?, ?, ?)",
                             (name, sequence, template_dna_name))
        self._connection_to_database.commit()

    def delete_by_template_dna_name(self, template_dna_name):
        """A method for deleting primers based on their template DNA's name

        Args:
            name: Name of the template DNA as a string
        """

        self._cursor.execute(
            "delete from primer where template_dna_name = ?", (template_dna_name,))
        self._connection_to_database.commit()

    def count_by_name_prefix_and_infix(self, prefix_and_infix):
        """Counts the rows with a certain prefix (template DNA name) and infix (_for or _rev)

        Args:
            prefix_and_infix: Primer name prefix and infix as a string
        Returns:
            The number of rows corresponding to the string given as a parameter
        """

        self._cursor.execute(
            "select count(*) from primer where name like ?", ('%' + prefix_and_infix + '%',))
        return self._cursor.fetchone()[0]

    def count_by_template_dna_name(self, template_dna_name):
        """Counts the rows from the table with a certain template DNA name

        Args:
            template_dna_name: Name of the template DNA as a string
        Returns:
            The number of rows corresponding to the string given as a parameter
        """

        self._cursor.execute(
            "select count(*) from primer where template_dna_name = ?", (template_dna_name,))
        return self._cursor.fetchone()[0]

    def find_by_sequence_and_template_dna_name(self, sequence, template_dna_name):
        """Fetches a primer tuple from the database based on the sequence and template DNA name

        Args:
            sequence: Nucleotide sequence of the primer to be fetched from the database
            template_dna_name: Name of the template DNA as a string
        """

        self._cursor.execute(
            "select * from primer where sequence = ? and template_dna_name = ?",
            (sequence, template_dna_name,))

        return self._cursor.fetchone()

    def find_all_by_template_dna_name(self, template_dna_name):
        """Fetches all rows from the table with a certain template_dna_name

        Args:
            template_dna_name: Name of the template dna as a string
        Returns:
            A list of tuples containing the primer information
        """

        self._cursor.execute(
            "select * from primer where template_dna_name = ?", (template_dna_name,))

        return self._cursor.fetchall()


primer_repository = PrimerRepository(get_connection_to_database())
