import unittest
import io
import sys


class StringConcatenationTest(unittest.TestCase):
    def testString(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        import prog_1_tp2_strings_concatenation

        strip = captured_output.getvalue().strip()
        self.assertEqual(strip, '''The result of Bangladesh comes first in the dictionary than Barbados is True.''')


if __name__ == "__main__":
    unittest.main()

