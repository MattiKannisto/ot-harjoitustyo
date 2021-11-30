import os
import sqlite3


def get_connection_to_database():
    directory_name = os.path.dirname(__file__)
    return sqlite3.connect(os.path.join(directory_name, "..", "data", "database.sqlite"))
