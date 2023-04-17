# Task
#
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while
# leaving the even numbers at their original positions.
#
# Examples
#
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# solution
def sort_array(source_array):
    for i in range(len(source_array)):
        for j in range(i + 1, len(source_array)):
            if source_array[i] % 2 != 0 and source_array[j] % 2 != 0:
                if source_array[i] > source_array[j]:
                    source_array[i], source_array[j] = source_array[j], source_array[i]
    return source_array


# tests
import unittest

class SortArrayBasicTests(unittest.TestCase):
    def test_sort_odd_numbers(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
    
    def test_empty_list_as_input(self):
        self.assertEqual(sort_array([]), [])


if __name__ == '__main__':
    unittest.main()
