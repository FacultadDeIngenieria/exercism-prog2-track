import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_5_strings_list import (
    last_name_first_letter,
    name_key,
)

class StringsListTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(last_name_first_letter("Ponce"), "El apellido Ponce comienza con una letra que está después de la M")

    def test_2(self):
        self.assertEqual(last_name_first_letter(""), "El apellido está vacío")

    def test_3(self):
        self.assertEqual(last_name_first_letter("Miodosky"), "El apellido Miodosky comienza con la letra M")

    def test_4(self):
        self.assertEqual(last_name_first_letter("Longo"), "El apellido Longo comienza con una letra que está antes de la M")

    def test_5(self):
        self.assertEqual(name_key("Agustín","Alexander"), "La clave generada es: AleAgustí")

    def test_6(self):
        self.assertEqual(name_key("Marcos","Paz"), "La clave generada es: PazMarco")

    def test_7(self):
        self.assertEqual(name_key("Luis","Re"), "La clave generada es: ReLui")

if __name__ == "__main__":
    unittest.main()
