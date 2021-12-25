import unittest
from repositories.account_repository import account_repository
import database_initialization


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        database_initialization.initialize()
        self.account_repository = account_repository
        self.name_1 = "test_name_1"
        self.password_1 = "test_p4ssW0rd_1"
        self.directory_1 = "/test/directory_1"
        self.primer_length_1 = 20
        self.primer_gc_content_1 = 0.5
        self.name_2 = "test_name_2"
        self.password_2 = "test_p4ssW0rd_2"
        self.directory_2 = "/test/directory_2"
        self.primer_length_2 = 15
        self.primer_gc_content_2 = 0.4

    def test_create(self):
        self.assertEqual(
            self.account_repository.find_by_name(self.name_1), None)
        self.account_repository.create(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_1, self.primer_gc_content_1)
        self.assertEqual(self.account_repository.find_by_name(
            self.name_1)[0], self.name_1)

    def test_delete(self):
        self.account_repository.create(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_1, self.primer_gc_content_1)
        self.assertEqual(self.account_repository.find_by_name(
            self.name_1)[0], self.name_1)
        self.account_repository.delete(self.name_1)
        self.assertEqual(
            self.account_repository.find_by_name(self.name_1), None)

    def test_find_by_name_returns_none_if_account_has_not_been_added_to_database(self):
        self.assertEqual(
            self.account_repository.find_by_name(self.name_1), None)

    def test_find_by_name_returns_correct_tuple_if_account_has_been_added_to_database(self):
        self.account_repository.create(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_1, self.primer_gc_content_1)
        self.assertEqual(self.account_repository.find_by_name(
            self.name_1)[0], self.name_1)

    def test_find_by_name_and_password_returns_none_if_account_has_not_been_added_to_database(self):
        self.assertEqual(self.account_repository.find_by_name_and_password(
            self.name_1, self.password_1), None)

    def test_find_by_name_returns_correct_tuple_with_correct_name_and_password(self):
        self.account_repository.create(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_1, self.primer_gc_content_1)
        self.assertEqual(self.account_repository.find_by_name_and_password(
            self.name_1, self.password_1)[0], self.name_1)

    def test_find_by_name_returns_none_with_correct_name_and_incorrect_password(self):
        self.account_repository.create(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_1, self.primer_gc_content_1)
        self.assertEqual(self.account_repository.find_by_name_and_password(
            self.name_1, self.password_2), None)

    def test_find_by_name_returns_none_with_incorrect_name_and_correct_password(self):
        self.account_repository.create(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_1, self.primer_gc_content_1)
        self.assertEqual(self.account_repository.find_by_name_and_password(
            self.name_2, self.password_1), None)

    def test_find_by_directory_returns_none_if_no_directory_has_been_added(self):
        self.assertEqual(self.account_repository.find_by_directory(
            self.directory_1), None)

    def test_find_by_directory_returns_correct_tuple_if_the_directory_has_been_added(self):
        self.account_repository.create(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_1, self.primer_gc_content_1)
        self.assertEqual(self.account_repository.find_by_directory(
            self.directory_1)[0], self.name_1)

    def test_update_changes_information_in_database(self):
        self.account_repository.create(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_1, self.primer_gc_content_1)
        self.account_repository.update(self.name_1, self.password_1, self.directory_1,
                                       self.primer_length_2, self.primer_gc_content_2)
        updated_account = self.account_repository.find_by_name(self.name_1)
        self.assertEqual(updated_account[3], self.primer_length_2)
