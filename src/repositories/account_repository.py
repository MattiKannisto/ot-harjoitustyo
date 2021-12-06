from entities.account import Account
from database_connection import get_connection_to_database


def get_account_row(row):
    account = Account(row["username"], row["password"],
                      row["directory"]) if row else None
    return account


class AccountRepository:
    def __init__(self, connection_to_database):
        self.connection_to_database = connection_to_database
        self.cursor = self.connection_to_database.cursor()

    def create(self, account):
        self.cursor.execute("insert into account (username, password, directory) values (?, ?)",
                            (account.username, account.password, account.directory))
        self.connection_to_database.commit()

    def find_by_name(self, username):
        self.cursor.execute(
            'select * from account where username = ?',
            (username,)
        )
        return self.cursor.fetchone()

    def find_all(self):
        self.cursor.execute("select * from account")
        return list(self.cursor.fetchall())


account_repository = AccountRepository(get_connection_to_database())
