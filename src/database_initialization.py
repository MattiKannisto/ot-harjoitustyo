from database_connection import get_connection_to_database


def drop_all_tables(cursor):
    """A method for dropping all tables

    Args:
        cursor: A cursor object for executing SQLite operations
    """

    cursor.execute('''
        drop table if exists account;
    ''')

    cursor.execute('''
        drop table if exists dna_fragment;
    ''')

    cursor.execute('''
        drop table if exists primer;
    ''')


def create_all_tables(cursor):
    """A method for creating all tables needed by the application

    Args:
        cursor: A cursor object for executing SQLite operations
    """

    cursor.execute('''
        create table account (
            name text primary key,
            password text,
            directory text,
            primer_length int,
            primer_gc_content float
        );
    ''')

    cursor.execute('''
        create table dna_fragment (
            name text primary key,
            for_strand text,
            rev_strand text,
            owner_name text
        );
    ''')

    cursor.execute('''
        create table primer (
            name text primary key,
            sequence text,
            template_dna_name text
        );
    ''')


def initialize():
    """A method for initializing the database
    """

    connection = get_connection_to_database()
    cursor = connection.cursor()

    drop_all_tables(cursor)
    create_all_tables(cursor)

    connection.commit()


if __name__ == "__main__":
    initialize()
