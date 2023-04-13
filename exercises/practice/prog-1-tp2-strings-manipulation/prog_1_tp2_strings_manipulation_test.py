import unittest
import io
import sys


class StringManipulationTest(unittest.TestCase):
    def testString(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        import prog_1_tp2_strings_manipulation

        strip = captured_output.getvalue().strip()
        self.assertEqual(strip, '''ada lovelace
Ada Lovelace
ADA LOVELACE
	ada lovelace''')


if __name__ == "__main__":
    unittest.main()

