import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_4_months import (
    number_to_month,
)


class MonthsTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(number_to_month(1), "enero")
        self.assertEqual(number_to_month(2), "febrero")
        self.assertEqual(number_to_month(3), "marzo")
        self.assertEqual(number_to_month(4), "abril")
        self.assertEqual(number_to_month(5), "mayo")
        self.assertEqual(number_to_month(6), "junio")
        self.assertEqual(number_to_month(7), "julio")
        self.assertEqual(number_to_month(8), "agosto")
        self.assertEqual(number_to_month(9), "septiembre")
        self.assertEqual(number_to_month(10), "octubre")
        self.assertEqual(number_to_month(11), "noviembre")
        self.assertEqual(number_to_month(12), "diciembre")
        self.assertEqual(number_to_month(13), "error")
        self.assertEqual(number_to_month(-1), "error")
        self.assertEqual(number_to_month(0), "error")


if __name__ == "__main__":
    unittest.main()
