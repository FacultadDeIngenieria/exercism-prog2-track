import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_4_sorting_countries import (
    x_is_before_than_y,
    y_is_before_than_x,
)

class HelloWorldTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(x_is_before_than_y("a", "b"), "The result of a comes first in the dictionary than b is True.")

    def test_2(self):
        self.assertEqual(x_is_before_than_y("b", "a"), "The result of a comes first in the dictionary than b is False.")

    def test_3(self):
        self.assertEqual(x_is_before_than_y("a", "b"), "The result of b comes first in the dictionary than a is False.")

    def test_4(self):
        self.assertEqual(x_is_before_than_y("b", "a"), "The result of b comes first in the dictionary than a is True.")

if __name__ == "__main__":
    unittest.main()
