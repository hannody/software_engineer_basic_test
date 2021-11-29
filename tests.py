"""
Developed by Mohanad Abu-Nayla, Nov-2021.
www.abunayla.com
This work comes without any warranty of any type, use it at your own risk.
If you find any thing useful, please send me a message/credit me, but you are 
not required to do so.
"""

import unittest
from task import Task


class TestTask(unittest.TestCase):
    """
    Tests for Task Class.
    """

    def setUp(self) -> None:
        """ 
        Mocks data for the tests 
        """
        self.testing_csv_file = "testing_output.csv"

    def test_uppercase(self):
        """
        Test for uppercase function.
        """
        self.assertEqual(Task().uppercase("hello"), "HELLO")
        self.assertEqual(Task().uppercase(""), "")
        self.assertEqual(Task().uppercase("HELLO"), "HELLO")
        self.assertEqual(Task().uppercase("hello woRld"), "HELLO WORLD")

    def test_altcase(self):
        """
        Test for altcase function.
        """
        self.assertEqual(Task().altcase(""), "")
        self.assertEqual(Task().altcase("hello"), "hElLo")
        self.assertEqual(Task().altcase("hello world"), "hElLo wOrLd")

    def test_csvexport(self):
        """
        Test for csvexport function.
        """
        self.assertEqual(Task().csvexport(
            self.testing_csv_file, ""), "CSV created!")
        self.assertEqual(Task().csvexport(
            self.testing_csv_file, "hello"), "CSV created!")
        self.assertEqual(Task().csvexport(
            self.testing_csv_file, "hello world"), "CSV created!")


if __name__ == '__main__':
    unittest.main()
