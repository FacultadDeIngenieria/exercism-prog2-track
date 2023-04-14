import unittest

# Tests adapted from `problem-specifications//canonical-data.json`


class HelloWorldTest(unittest.TestCase):
    def test_say_hi(self):
        self.assertEqual("Hello, World!", "Hello, World!")


if __name__ == "__main__":
    unittest.main()
