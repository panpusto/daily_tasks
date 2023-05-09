# Your task is to write function factorial.
# https://en.wikipedia.org/wiki/Factorial

# solution_1
from itertools import accumulate as acc
import operator

def factorial_with_itertools(n):
    lst_iter = acc([num for num in range(1, n + 1)], func=operator.mul)
    return [num for num in lst_iter][-1] if n > 1 else 1


# solution_2
import math

def factorial_with_math(n):
    return math.factorial(n)


# solution_3
def factorial_with_simple_loop(n):
    result = 1
    for num in range(1, n + 1):
        result *= num

    return result


# tests
import unittest

class FactorialBasicTests(unittest.TestCase):
    def test_factorial_with_iter(self):
        self.assertEqual(factorial_with_itertools(0), 1)
        self.assertEqual(factorial_with_itertools(1), 1)
        self.assertEqual(factorial_with_itertools(5), 120)
        self.assertEqual(factorial_with_itertools(10), 3628800)
        self.assertEqual(factorial_with_itertools(20), 2.43290200817664e18)
    
    def test_factorial_with_math(self):
        self.assertEqual(factorial_with_math(0), 1)
        self.assertEqual(factorial_with_math(1), 1)
        self.assertEqual(factorial_with_math(5), 120)
        self.assertEqual(factorial_with_math(10), 3628800)
        self.assertEqual(factorial_with_math(20), 2.43290200817664e18)
    
    def test_factorial_with_loop(self):
        self.assertEqual(factorial_with_simple_loop(0), 1)
        self.assertEqual(factorial_with_simple_loop(1), 1)
        self.assertEqual(factorial_with_simple_loop(5), 120)
        self.assertEqual(factorial_with_simple_loop(10), 3628800)
        self.assertEqual(factorial_with_simple_loop(20), 2.43290200817664e18)


if __name__ == '__main__':
    unittest.main()
