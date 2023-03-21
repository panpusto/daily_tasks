# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1

# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# we want to find a positive integer k, if it exists, 
# such that the sum of the digits of n taken to the successive powers of p is equal to k * n.

# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case we will return k, if not return -1.
# Note: n and p will always be given as strictly positive integers.

# solution
import unittest

def dig_pow(n, p):
    str_num = str(n)
    total = 0
    for i, j in enumerate(range(p, p + len(str_num))):
        total += int(str_num[i]) ** j
    return total//n if total % n == 0 else -1
        
    
# tests
class TestDigPow(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(dig_pow(89, 1), 1)

    def test_case_2(self):
        self.assertEqual(dig_pow(92, 1), -1)

    def test_case_3(self):
        self.assertEqual(dig_pow(46288, 3), 51)

    def test_case_4(self):
        self.assertEqual(dig_pow(41, 5), 25)

    def test_case_5(self):
        self.assertEqual(dig_pow(114, 3), 9)

    def test_case_6(self):
        self.assertEqual(dig_pow(8, 3), 64)


if __name__ == '__main__':
    unittest.main()