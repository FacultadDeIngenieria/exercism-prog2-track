import unittest
import io
import sys


class StringInputTest(unittest.TestCase):
    def testString(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        import prog_1_tp2_strings_input

        strip = captured_output.getvalue().strip()
        self.assertEqual(strip, '''Ingresar gasto:
23.75
Dinero recibido
100

Vuelto

Pesos:
76
Centavos:
25''')

if __name__ == "__main__":
    unittest.main()

