import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_5_calculating_change import (
    calculate_integer_part_of_change,
    calculate_cents_part_of_change,
)

class HelloWorldTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calculate_integer_part_of_change(100, 101.5), 1)

    def test_2(self):
        self.assertEqual(calculate_integer_part_of_change(100, 100.5), 0)

    def test_3(self):
        self.assertEqual(calculate_cents_part_of_change(100, 101.5), 50)

    def test_4(self):
        self.assertEqual(calculate_cents_part_of_change(100, 101), 0)

if __name__ == "__main__":
    unittest.main()
