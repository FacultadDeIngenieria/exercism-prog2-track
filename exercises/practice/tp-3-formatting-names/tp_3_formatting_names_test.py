import unittest

class StringManipulationTest(unittest.TestCase):
    def testString(self):
        self.assertEqual("Hello, World!", "Hello, World!")

if __name__ == "__main__":
    unittest.main()

