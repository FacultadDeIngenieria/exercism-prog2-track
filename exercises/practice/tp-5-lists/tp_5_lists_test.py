import unittest

# Tests adapted from `problem-specifications//canonical-data.json`

from tp_5_lists import (
    remove_elements,
    add_elements,
    is_empty,
    check_lists,
    list_of_lists
)

class ListsTest(unittest.TestCase):

    input_1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    input_2 = ['Red', 'Green', 'White', 'Black']
    input_3 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
    input_4 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
    input_5 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
    def test_1(self):
        removed = remove_elements(self.input_1.copy())
        self.assertEqual(len(removed), 3)
        self.assertEqual(removed[0], self.input_1[1])
        self.assertEqual(removed[1], self.input_1[2])
        self.assertEqual(removed[2], self.input_1[3])

    def test_2(self):
        removed = remove_elements(self.input_1[:3].copy())
        self.assertEqual(len(removed), 2)
        self.assertEqual(removed[0], self.input_1[1])
        self.assertEqual(removed[1], self.input_1[2])

    def test_3(self):
        added = add_elements(self.input_2.copy())
        self.assertEqual(len(added), 6)
        self.assertEqual(added[0], "Pink")
        self.assertEqual(added[-1], "Yellow")

    def test_4(self):
        added = add_elements([])
        self.assertEqual(len(added), 2)
        self.assertEqual(added[0], "Pink")
        self.assertEqual(added[1], "Yellow")

    def test_5(self):
        self.assertEqual(is_empty([]), True)
        self.assertEqual(is_empty(self.input_1.copy()), False)

    def test_6(self):
        self.assertEqual(check_lists(self.input_3, self.input_4), True)
        self.assertEqual(check_lists(self.input_3, self.input_1), False)
        self.assertEqual(check_lists(self.input_3, self.input_3[:2]), False)

    def test_7(self):
        array = list_of_lists(self.input_5.copy())
        self.assertEqual(len(array), 3)

        self.assertEqual(len(array[0]), 2)
        self.assertEqual(array[0][0], self.input_5[0][0])
        self.assertEqual(array[0][1], self.input_5[0][1])

        self.assertEqual(len(array[1]), 3)
        self.assertEqual(array[1][0], self.input_5[1][1])
        self.assertEqual(array[1][1], self.input_5[1][2])
        self.assertEqual(array[1][2], self.input_5[1][3])

        self.assertEqual(len(array[2]), 2)
        self.assertEqual(array[2][0], self.input_5[2][2])
        self.assertEqual(array[2][1], self.input_5[2][3])


    def test_8(self):
        array_1 = list_of_lists([])
        self.assertEqual(len(array_1), 0)
        array_2 = list_of_lists([[],[],[]])
        self.assertEqual(len(array_2), 3)
        self.assertEqual(len(array_2[0]), 0)
        self.assertEqual(len(array_2[1]), 0)
        self.assertEqual(len(array_2[2]), 0)




if __name__ == "__main__":
    unittest.main()
