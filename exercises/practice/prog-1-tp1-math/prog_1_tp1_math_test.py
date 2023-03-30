import unittest

from prog_1_tp1_math import tp1

class MathTest(unittest.TestCase):
    def test(self):
        self.assertEqual(tp1(), 57 * 7)


if __name__ == "__main__":
    unittest.main()

