import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_7_recursive import (
    put, remove, index_of_empty, index_of_by_index, index_of
)


class LoopsTest(unittest.TestCase):

    golden = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
    golden_with_empty = ["Red", "Green", "", "", "Pink", "", "Black"]

    def test_1(self):
        self.assertEqual(index_of("Red", self.golden.copy()), 0)
        self.assertEqual(index_of("Blue", self.golden.copy()), -1)
        self.assertEqual(index_of("Black", self.golden.copy()), 3)

    def test_2(self):
        self.assertEqual(index_of_by_index("Black", self.golden.copy(), 1), 3)
        self.assertEqual(index_of_by_index("Black", self.golden.copy(), 4), 6)
        self.assertEqual(index_of_by_index("Green", self.golden.copy(), 2), -1)
        self.assertEqual(index_of_by_index("Yellow", self.golden.copy(), 0), 5)

    def test_empty(self):
        self.assertEqual(index_of_by_index("Yellow", [], 0), -1)
        self.assertEqual(index_of("Black", []), -1)
        self.assertEqual(index_of_empty([]), -1)
        self.assertEqual(put("Black", []), -1)
        self.assertEqual(remove("Black", []), 0)

    def test_3(self):
        self.assertEqual(index_of_empty(self.golden_with_empty.copy()), 2)
        self.assertEqual(index_of_empty(self.golden.copy()), -1)

    def test_4(self):
        self.assertEqual(put("Blue", self.golden_with_empty.copy()), 2)
        self.assertEqual(put("Blue", self.golden.copy()), -1)

    def test_5(self):
        self.assertEqual(remove("Black", self.golden.copy()), 2)
        self.assertEqual(remove("Blue", self.golden.copy()), 0)


if __name__ == "__main__":
    unittest.main()
