import unittest
from services.account_service import AccountService


class MockUpAccountRepository:
    def __init__(self):
        self.accounts = []

    def create(self, name, password, directory, primer_length, primer_gc_content):
        self.accounts.append((name, password, directory, str(
            primer_length), str(primer_gc_content)))

    def find_by_name(self, name):
        for account in self.accounts:
            if account[0] == name:
                return account
        return None

    def find_by_directory(self, directory):
        for account in self.accounts:
            if account[2] == directory:
                return account
        return None


class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.account_service = AccountService(MockUpAccountRepository())
        self.name = "test_name"
        self.password = "test_p4ssW0rd"
        self.directory = "/test/directory"

    def test_create_account_adds_an_account_to_database(self):
        self.account_service.create_account(
            self.name, self.password, self.password, self.directory, [])
        self.assertEqual(self.account_service.get_account_by_name(
            self.name).name, self.name)

    def test_name_already_in_use_returns_false_if_name_is_not_already_in_use(self):
        self.assertEqual(
            self.account_service.name_already_in_use(self.name), False)

    def test_name_already_in_use_returns_true_if_name_is_already_in_use(self):
        self.account_service.create_account(
            self.name, self.password, self.password, self.directory, [])
        self.assertEqual(
            self.account_service.name_already_in_use(self.name), True)
