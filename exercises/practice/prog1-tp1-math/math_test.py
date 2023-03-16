import unittest
import io
import sys

class MathTest(unittest.TestCase):
    def test(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        import math_exercise

        strip = captured_output.getvalue().strip()
        self.assertEqual(strip, '''64
50
399
32.0
8
1
8.142857142857142''')


if __name__ == "__main__":
    unittest.main()

