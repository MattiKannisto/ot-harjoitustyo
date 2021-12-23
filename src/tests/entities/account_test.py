import unittest
from entities.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.name = "test_name"
        self.password = "test_p4ssW0rd"
        self.directory = "/test/directory"
        self.default_primer_length = 20
        self.default_primer_gc_content = 0.5
        self.custom_primer_length = 25
        self.custom_primer_gc_content = 0.6
        self.account_with_default_primer_settings = Account(
            self.name, self.password, self.directory)
        self.account_with_custom_primer_settings = Account(
            self.name, self.password, self.directory, self.custom_primer_length, self.custom_primer_gc_content)

    def test_newly_created_account_has_correct_name(self):
        self.assertEqual(
            self.account_with_default_primer_settings.name, self.name)

    def test_newly_created_account_has_correct_password(self):
        self.assertEqual(self.account_with_default_primer_settings.password,
                         self.password)

    def test_newly_created_account_has_correct_directory(self):
        self.assertEqual(self.account_with_default_primer_settings.directory,
                         self.directory)

    def test_newly_created_has_a_default_primer_length_of_20(self):
        self.assertEqual(self.account_with_default_primer_settings.primer_length,
                         self.default_primer_length)

    def test_newly_created_has_a_default_gc_content_of_zero_point_five(self):
        self.assertEqual(self.account_with_default_primer_settings.primer_gc_content,
                         self.default_primer_gc_content)

    def test_primer_length_can_be_set_to_desired_value(self):
        self.assertEqual(self.account_with_custom_primer_settings.primer_length,
                         self.custom_primer_length)

    def test_primer_gc_content_can_be_set_to_desired_value(self):
        self.assertEqual(self.account_with_custom_primer_settings.primer_gc_content,
                         self.custom_primer_gc_content)
