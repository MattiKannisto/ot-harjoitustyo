from entities.dna_fragment import DnaFragment
from database_connection import get_connection_to_database


def get_dna_fragment_row(row):
    dna_fragment = DnaFragment(row["name"], row["sequence"]) if row else None
    return dna_fragment


class DnaFragmentRepository:
    def __init__(self, connection_to_database):
        self.connection_to_database = connection_to_database
        self.cursor = self.connection_to_database.cursor()

    def create(self, name, sequence):
        self.cursor.execute("insert into dna_fragment (name, sequence) values (?, ?)",
                            (name, sequence))
        self.connection_to_database.commit()

    def find_by_name(self, name):
        self.cursor.execute(
            'select * from dna_fragment where name = ?',
            (name,)
        )
        return self.cursor.fetchone()

    def find_all(self):
        self.cursor.execute("select * from dna_fragment")
        return list(self.cursor.fetchall())


dna_fragment_repository = DnaFragmentRepository(get_connection_to_database())
