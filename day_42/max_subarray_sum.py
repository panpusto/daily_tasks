# The maximum sum subarray problem consists in finding the maximum sum of a
# contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and
# the maximum sum is the sum of the whole array. If the list is made up
# of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the
# empty list or array is also a valid sublist/subarray.

# solution
def max_sequence(arr):
    if not arr or all(num < 0 for num in arr):
        return 0
    
    max_seq_sum = float('-inf')
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i + 1, len(arr)):
            curr_sum += arr[j]
            if curr_sum > max_seq_sum:
                max_seq_sum = curr_sum       
    return max_seq_sum

# more optimised solution with Kadane's algorithm (time comlexity O(n))
def max_sequence_kadane(arr):
    if not arr or all(num < 0 for num in arr):
        return 0
    
    max_sum = float('-inf')
    curr_sum = 0

    for num in arr:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

# tests
import unittest

class MaxSubArrSumBasicTests(unittest.TestCase):
    def test_max_sum_of_seq(self):
        self.assertEqual(max_sequence([]), 0)
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)

    def test_max_sum_of_seq_kadane(self):
        self.assertEqual(max_sequence_kadane([]), 0)
        self.assertEqual(max_sequence_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sequence_kadane([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)


if __name__ == '__main__':
    unittest.main()
