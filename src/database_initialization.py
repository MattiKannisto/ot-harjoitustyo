from database_connection import get_connection_to_database


def drop_all_tables(cursor):
    cursor.execute('''
        drop table if exists account;
    ''')

    cursor.execute('''
        drop table if exists dna_fragment;
    ''')


def create_all_tables(cursor):
    cursor.execute('''
        create table account (
            username text primary key,
            password text
        );
    ''')

    cursor.execute('''
        create table dna_fragment (
            name text primary key,
            sequence text
        );
    ''')


def initialize():
    connection = get_connection_to_database()
    cursor = connection.cursor()

    drop_all_tables(cursor)
    create_all_tables(cursor)

    connection.commit()


if __name__ == "__main__":
    initialize()
