import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_4_quadratic import (
    roots,
    value_y,
    to_string,
    derivation
)


class QuadraticTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(roots(1, 0, 0), "(0.0)")

    def test_2(self):
        self.assertEqual(roots(1, 0, 2), "()")

    def test_3(self):
        self.assertEqual(roots(1, 1, 0), "(0.0,-1.0)")

    def test_4(self):
        self.assertEqual(roots(1, 0, 1), "()")

    def test_5(self):
        self.assertEqual(roots(1, 0, -1), "(1.0,-1.0)")

    def test_6(self):
        self.assertEqual(value_y(0, 0, 0, 4), 0)

    def test_7(self):
        self.assertEqual(value_y(3, 2, 1, -4), 41.0)

    def test_8(self):
        self.assertEqual(to_string(3, 2, 1), "Y = 3 * X2 + 2 * X + 1")

    def test_9(self):
        self.assertEqual(to_string(0, 0, 0), "Y = 0 * X2 + 0 * X + 0")

    def test_10(self):
        self.assertEqual(to_string(-3, 5, 4), "Y = -3 * X2 + 5 * X + 4")

    def test_11(self):
        self.assertEqual(derivation(2,4), "Y' = 2 * X + 4")

    def test_12(self):
        self.assertEqual(derivation(0,0), "Y' = 0 * X + 0")

    def test_13(self):
        self.assertEqual(derivation(-1,2), "Y' = -1 * X + 2")


if __name__ == "__main__":
    unittest.main()
