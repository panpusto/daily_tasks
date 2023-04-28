# Determine the total number of digits in the integer (n>=0) given as input to the function.
# For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. 
# Be careful to avoid overflows/underflows.
# All inputs will be valid.

# solution
def digits(n):
    if isinstance(n, str):
        return 0
    elif n <= 0:
        return 0
    return sum([elem.isdigit() for elem in list(str(n))])


# tests
import unittest

class DigitsCounterBasicTests(unittest.TestCase):
    def test_count_digits_in_positive_integer(self):
        self.assertEqual(digits(5), 1)
        self.assertEqual(digits(12345), 5)
        self.assertEqual(digits(9876543210), 10)
    
    def test_count_digits_in_negative_integer(self):
        self.assertEqual(digits(-987), 0)
    
    def test_count_digits_with_non_digit_parameter(self):
        self.assertEqual(digits('not integer'), 0)

    def test_count_digits_with_positive_floats(self):
        self.assertEqual(digits(21.37), 4)    

    def test_count_digits_with_negative_floats(self):
        self.assertEqual(digits(-21.37), 0)    


if __name__ == '__main__':
    unittest.main()
