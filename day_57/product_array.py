# Task
# Given an array/list [] of integers , Construct a product array Of same size
# Such That prod[i] is equal to The Product of all the elements of Arr[] 
# except Arr[i].

# Notes
# Array/list size is at least 2 .
# Array/list's numbers Will be only Positives
# Repetition of numbers in the array/list could occur.

# Input >> Output 

# Examples

# productArray ({12,20}) ==>  return {20,12}
# Explanation:
# The first element in prod [] array 20 is the product of all array's elements except the first element
# The second element 12 is the product of all array's elements except the second element .

# productArray ({1,5,2}) ==> return {10,2,5}
# Explanation:
# The first element 10 is the product of all array's elements except the first element 1
# The second element 2 is the product of all array's elements except the second element 5
# The Third element 5 is the product of all array's elements except the Third element 2.

# productArray ({10,3,5,6,2}) return ==> {180,600,360,300,900}
# Explanation:
# The first element 180 is the product of all array's elements except the first element 10
# The second element 600 is the product of all array's elements except the second element 3
# The Third element 360 is the product of all array's elements except the third element 5
# The Fourth element 300 is the product of all array's elements except the fourth element 6
# Finally ,The Fifth element 900 is the product of all array's elements except the fifth element 2


# solution without built-in functions
def product_array_non_builtin(numbers: list[int]) -> list[int]:
    result = []
    total = numbers[0]

    for i in range(1, len(numbers)):
        total *= numbers[i]
    
    for num in range(len(numbers)):
        result.append(total // numbers[num])
    
    return result


# solution with built-in functions
import math

def product_array(numbers: list[int]) -> list[int]:
    total = math.prod(numbers)
    return [total // num for num in numbers]


# tests
import unittest

class ProductArrayTests(unittest.TestCase):
    test_cases = [
        ([12,20], [20,12]),
        ([3,27,4,2], [216,24,162,324]),
        ([13,10,5,2,9], [900,1170,2340,5850,1300]),
        ([16,17,4,3,5,2], [2040,1920,8160,10880,6528,16320]),
    ]

    def test_product_array_without_builtin_funcs(self):
        for tested, expected in self.test_cases:
            self.assertEqual(product_array_non_builtin(tested), expected)

    def test_product_array_with_builtin_funcs(self):
        for tested, expected in self.test_cases:
            self.assertEqual(product_array(tested), expected)


if __name__ == '__main__':
    unittest.main()
