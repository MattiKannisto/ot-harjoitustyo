import unittest
from services.account_service import AccountService
import database_initialization


class TestAccountService(unittest.TestCase):
    def setUp(self):
        database_initialization.initialize()
        self.account_service = AccountService()
        self.username = "test_username"
        self.password = "test_p4ssW0rd"
        self.directory = "/test/directory"

    def test_create_account_adds_an_account_to_database(self):
        self.account_service.create_account(
            self.username, self.password, self.directory)
        self.assertEqual(self.account_service.get_account_by_name(
            self.username).username, self.username)

    def test_username_already_in_use_returns_false_if_username_is_not_already_in_use(self):
        self.assertEqual(
            self.account_service.username_already_in_use(self.username), False)

    def test_username_already_in_use_returns_true_if_username_is_already_in_use(self):
        self.account_service.create_account(
            self.username, self.password, self.directory)
        self.assertEqual(
            self.account_service.username_already_in_use(self.username), True)
