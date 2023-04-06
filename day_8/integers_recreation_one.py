# 1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.
# Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.
# The sum of these squares is 84100 which is 290 * 290.

# Task
# Find all integers between m and n (m and n integers with 1 <= m <= n) such
# that the sum of their squared divisors is itself a square.

# We will return an array of subarrays or of tuples (in C an array of Pair) or a string.
# The subarrays (or tuples or Pairs) will have two elements: 
# first the number the squared divisors of which is a square and then the sum of the squared divisors.

# Example:
# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]

# solution
import math
import unittest


def get_divisors(num):
    divisors = set()
    for divisor in range(1, int(math.sqrt(num) + 1)):
        if num % divisor == 0:
            divisors.add(divisor)
            divisors.add(int(num / divisor))
    total = sum(list(map(lambda x: x**2, list(divisors))))
    if (int(math.sqrt(total)) ** 2 == total) and total > 0:
        return [num, total]
    return False

def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        x = get_divisors(num)
        if x:
            result.append(x)
    return result



# tests
class ListSquaredTests(unittest.TestCase):
    def test_list_squared_func(self):
        self.assertEqual(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])
        self.assertEqual(list_squared(250, 500), [[287, 84100]])


if __name__ == '__main__':
    unittest.main()
