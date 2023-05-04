import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_6_loops import (
    enumerate_list,
    enumerate_backwards,
)


class LoopsTest(unittest.TestCase):

    input_1 = ["Red", "Green", "", "White", "Black"]

    def test_1(self):
        enumerated = enumerate_list(self.input_1.copy())
        self.assertEqual(len(enumerated), 4)
        self.assertEqual(enumerated[0], "0.\tRed")
        self.assertEqual(enumerated[1], "1.\tGreen")
        self.assertEqual(enumerated[2], "2.\tWhite")
        self.assertEqual(enumerated[3], "3.\tBlack")

    def test_2(self):
        enumerated = enumerate_list(self.input_1[:3].copy())
        self.assertEqual(len(enumerated), 2)
        self.assertEqual(enumerated[0], "0.\tRed")
        self.assertEqual(enumerated[1], "1.\tGreen")

    def test_3(self):
        enumerated = enumerate_list([])
        self.assertEqual(len(enumerated), 0)

    def test_4(self):
        enumerated = enumerate_backwards(self.input_1.copy())
        self.assertEqual(len(enumerated), 4)
        self.assertEqual(enumerated[0], "0.\tdeR")
        self.assertEqual(enumerated[1], "1.\tneerG")
        self.assertEqual(enumerated[2], "2.\tetihW")
        self.assertEqual(enumerated[3], "3.\tkcalB")

    def test_5(self):
        enumerated = enumerate_backwards(self.input_1[:3].copy())
        self.assertEqual(len(enumerated), 2)
        self.assertEqual(enumerated[0], "0.\tdeR")
        self.assertEqual(enumerated[1], "1.\tneerG")

    def test_6(self):
        enumerated = enumerate_backwards([])
        self.assertEqual(len(enumerated), 0)


if __name__ == "__main__":
    unittest.main()
