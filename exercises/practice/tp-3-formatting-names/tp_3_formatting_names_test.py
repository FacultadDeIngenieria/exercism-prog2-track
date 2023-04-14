import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_3_formatting_names import (
    all_lower_case,
    initial_as_upper_case,
    all_upper_case,
    tabbed
)

class HelloWorldTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(all_lower_case(), "ada lovelace")
    def test_2(self):
        self.assertEqual(initial_as_upper_case(), "Ada Lovelace")
    def test_3(self):
        self.assertEqual(all_upper_case(), "ADA LOVELACE")
    def test_4(self):
        self.assertEqual(tabbed(), "\tada lovelace")


if __name__ == "__main__":
    unittest.main()
