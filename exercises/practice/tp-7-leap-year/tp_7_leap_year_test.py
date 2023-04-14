import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_7_leap_year import (
    is_leap_year
)

class LeapYearTest(unittest.TestCase):
    def test_1(self):
        year = 2000
        self.assertEqual(is_leap_year(year),f"El año {year} es bisiesto")

    def test_2(self):
        year = 2001
        self.assertEqual(is_leap_year(year),f"El año {year} no es bisiesto")

    def test_3(self):
        year = 400
        self.assertEqual(is_leap_year(year),f"El año {year} es bisiesto")

    def test_4(self):
        year = 200
        self.assertEqual(is_leap_year(year),f"El año {year} no es bisiesto")

    def test_5(self):
        year = 8
        self.assertEqual(is_leap_year(year),f"El año {year} es bisiesto")


if __name__ == "__main__":
    unittest.main()
