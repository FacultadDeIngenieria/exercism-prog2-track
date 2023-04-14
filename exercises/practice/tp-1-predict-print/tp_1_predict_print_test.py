import unittest

class Test(unittest.TestCase):
    def test_say_hi(self):
        self.assertEqual("Hello, World!", "Hello, World!")


if __name__ == "__main__":
    unittest.main()
