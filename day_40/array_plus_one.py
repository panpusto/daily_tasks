# Given an array of integers of any length, return an array that has 1 added
# to the value represented by the array.
# the array can't be empty
# only non-negative, single digit integers are allowed

# Return nil (or your language's equivalent) for invalid inputs.

# Examples

# Valid arrays
# [4, 3, 2, 5] would return [4, 3, 2, 6]
# [1, 2, 3, 9] would return [1, 2, 4, 0]
# [9, 9, 9, 9] would return [1, 0, 0, 0, 0]
# [0, 1, 3, 7] would return [0, 1, 3, 8]

# Invalid arrays
# [1, -9] is invalid because -9 is not a non-negative integer
# [1, 2, 33] is invalid because 33 is not a single-digit integer


# solution
def up_array(arr):
    if any(num < 0 or num > 9 for num in arr) or not arr:
        return None

    next_num = int(''.join([str(num) for num in arr])) + 1
    if len(arr) == len(str(next_num)):
        return [int(num) for num in str(next_num)]
    
    result_arr = []
    prev_zeros = len(arr) - len(str(next_num))
    for i in range(prev_zeros):
        result_arr.append(0)
    return result_arr + [int(num) for num in str(next_num)]


# tests
import unittest

class UpArrayBasicTests(unittest.TestCase):
    def test_up_array_with_valid_input(self):
        self.assertEqual(up_array([2,3,9]), [2,4,0])
        self.assertEqual(up_array([9,9]), [1,0,0])
        self.assertEqual(up_array([0,4,2]), [0,4,3])
        self.assertEqual(up_array([4,3,2,5]), [4,3,2,6])
        self.assertEqual(up_array([1,2,3,9]), [1,2,4,0])
        self.assertEqual(up_array([9,9,9,9]), [1,0,0,0,0])
        self.assertEqual(up_array([0,1,3,7]), [0,1,3,8])
        self.assertEqual(up_array([5,7,4]), [5,7,5])
        self.assertEqual(up_array([0]), [1])
        self.assertEqual(up_array([1,0,0,0]), [1,0,0,1])
        self.assertEqual(up_array([9,9,9]), [1,0,0,0])
        self.assertEqual(up_array([2, 1, 4, 7, 4, 8, 3, 6, 4, 7]), [2, 1, 4, 7, 4, 8, 3, 6, 4, 8])

    def test_up_array_with_invalid_input(self):
        self.assertEqual(up_array([1,-9]), None)
        self.assertEqual(up_array([1,2,33]), None)
        self.assertEqual(up_array([1,2,-1]), None)
        self.assertEqual(up_array([10]), None)
        self.assertEqual(up_array([]), None)


if __name__ == '__main__':
    unittest.main()
