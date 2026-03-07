import unittest
from homework12 import sum_of_even_numbers,has_h_in_both_cases,check_text_length

class TestSumOfEvenNumbers(unittest.TestCase):

    def test_basic_even_sum(self):
        self.assertEqual(sum_of_even_numbers([1, 2, 3, 4, 5, 6]), 12)

    def test_empty_list(self):
        self.assertEqual(sum_of_even_numbers([]), 0)

    def test_all_odd_numbers(self):
        self.assertEqual(sum_of_even_numbers([1, 3, 5, 7, 9]), 0)

    def test_negative_and_zero(self):
        self.assertEqual(sum_of_even_numbers([-4, -2, 0, 1, 3, 5]), -6)

class TestHasHInBothCases(unittest.TestCase):

    def test_contains_both_cases(self):
        self.assertTrue(has_h_in_both_cases("Hello"))
        self.assertTrue(has_h_in_both_cases("hH"))
        self.assertTrue(has_h_in_both_cases("The House has History"))
        self.assertTrue(has_h_in_both_cases("hola Hola"))

    def test_no_h_at_all_and_edge_cases(self):
        self.assertFalse(has_h_in_both_cases("python3"))
        self.assertFalse(has_h_in_both_cases("12345"))
        self.assertFalse(has_h_in_both_cases("!@#$%^&*"))
        self.assertFalse(has_h_in_both_cases(""))
        self.assertFalse(has_h_in_both_cases("   "))
        self.assertFalse(has_h_in_both_cases("Привіт"))

class TestCheckTextLength(unittest.TestCase):

    def test_length_10(self):
        self.assertEqual(check_text_length("1234567890"), "True")
        self.assertEqual(check_text_length("Hello world!"), "True")
        self.assertEqual(check_text_length("a"*15), "True")

    def test_length_lt_10_not_empty(self):
        self.assertEqual(check_text_length("123456789"), "False")
        self.assertEqual(check_text_length("abc"), "False")
        self.assertEqual(check_text_length(" "), "False")

    def test_empty_string(self):
        self.assertEqual(check_text_length(""), "Поле не може бути пустим")
        self.assertEqual(check_text_length("   ".strip()), "Поле не може бути пустим")


if __name__ == '__main__':
    unittest.main()