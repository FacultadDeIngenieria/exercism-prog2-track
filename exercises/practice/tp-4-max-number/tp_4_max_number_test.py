import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_4_max_number import (
    max_of_two,
    max_of_three,
)


class MaxNumberTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(max_of_two(1, 2), 2)

    def test_2(self):
        self.assertEqual(max_of_two(3, 2), 3)

    def test_3(self):
        self.assertEqual(max_of_two(4, 4), 4)

    def test_4(self):
        self.assertEqual(max_of_two(-5, -10), -5)

    def test_5(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)

    def test_6(self):
        self.assertEqual(max_of_three(4, 6, 5), 6)

    def test_7(self):
        self.assertEqual(max_of_three(9, -6, 8), 9)

    def test_8(self):
        self.assertEqual(max_of_three(-5, -5, -5), -5)


if __name__ == "__main__":
    unittest.main()
