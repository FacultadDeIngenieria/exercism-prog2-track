import unittest
import io
import sys

class VariablesTest(unittest.TestCase):
    def test(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        import variables

        strip = captured_output.getvalue().strip()
        self.assertEqual(strip, '''Hello,
valor de i1:
3
valor de i2:
5
valor de i3:
8
16
Python is awesome
valor de x: Naranja, valor de y: Naranja, valor de z: Naranja
1.6
3
entero i3:
9
variable f3:
9.5
el valor de
13
más
-0.5
es:
12.5''')


if __name__ == "__main__":
    unittest.main()

