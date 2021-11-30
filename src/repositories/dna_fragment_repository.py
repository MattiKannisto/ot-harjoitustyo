from entities.dna_fragment import DnaFragment
from database_connection import get_database_connection


class DnaFragmentRepository:
    def __init__(self, connection_to_database):
        self.connection_to_database = connection_to_database

    def create(self, dna_fragment):
        cursor = self.connection_to_database.cursor()

        cursor.execute("insert into dna_fragment (name, sequence) values (?, ?)"), (dna_fragment.name, dna_fragment.sequence))

        self.connection_to_database.commit()

    def find_by_name(self, name):
        cursor=self._connection.cursor()

        cursor.execute(
            'select * from dna_fragment where name = ?',
            (name,)
        )

        return get_user_by_row(cursor.fetchone())

dna_fragment_repository=DnaFragmentRepository(get_connection_to_database())
