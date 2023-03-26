import unittest

from prueba import (
    hello,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class HelloWorldTest(unittest.TestCase):
    def test_say_hi(self):
        self.assertEqual(hello(), "Hello, World!")
        self.assertTrue(self, True)


if __name__ == "__main__":
    unittest.main()
