# Complete the method which returns the number which is most frequent in the
# given input array. If there is a tie for most frequent number, return the
# largest number among them.
# Note: no empty arrays will be given.

# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

# solution_1
from collections import Counter

def highest_rank(arr):
    frequency = Counter(arr)

    most_frequent_num = None
    max_frequency = 0

    for num, freq in frequency.items():
        if freq > max_frequency or (freq == max_frequency and num > most_frequent_num):
            most_frequent_num = num
            max_frequency = freq
    
    return most_frequent_num

# solution_2
def highest_rank2(arr):
    frequency = Counter(arr)
    max_freq = max(frequency.values())
    return max([num for num, freq in frequency.items() if freq == max_freq])


# tests
import unittest

class HighestRankNumberBasicTests(unittest.TestCase):
    def test_find_most_frequent_number(self):
        self.assertEqual(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
        self.assertEqual(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
        self.assertEqual(highest_rank([1, 2, 3]), 3)
    
    def test_find_most_frequent_number_ver_2(self):
        self.assertEqual(highest_rank2([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
        self.assertEqual(highest_rank2([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
        self.assertEqual(highest_rank2([1, 2, 3]), 3)


if __name__ == '__main__':
    unittest.main()
