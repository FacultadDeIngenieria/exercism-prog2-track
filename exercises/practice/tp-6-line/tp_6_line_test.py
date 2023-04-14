import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_6_line import (
    equation_to_string,
    point_to_string,
    distance
)

class LineEquationTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(equation_to_string(1, 2), "Y = 1x  + 2")

    def test_2(self):
        self.assertEqual(equation_to_string(-1, -2), "Y = -1x  + -2")

    def test_3(self):
        self.assertEqual(point_to_string(1, 1, 0), "(0, 1)")

    def test_4(self):
        self.assertEqual(point_to_string(1, 1, 1), "(0, 2)")

    def test_5(self):
        self.assertEqual(distance(1, 1, 0, 3), 5)


if __name__ == "__main__":
    unittest.main()
