# Given a positive number n > 1 find the prime factor decomposition of n.
# The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

###############################################################################

# solution
def prime_factors(num: int) -> str:
    result = []
    i = 2

    while i * i <= num:
        count = 0
        while num % i == 0:
            num //= i
            count += 1
        if count > 0:
            result.append((i, count))
        if i == 2:
            i = 3
        else:
            i += 2
    
    if num > 1:
        result.append((num, 1))
    
    prime_factors_str = ''
    for factor, exponent in result:
        if exponent == 1:
            prime_factors_str += f"({factor})"
        else:
            prime_factors_str += f"({factor}**{exponent})"
    
    return prime_factors_str


# tests
import unittest

class PrimeFactorsTests(unittest.TestCase):
    test_cases = [
        (7775460, "(2**2)(3**3)(5)(7)(11**2)(17)"),
        (7919, "(7919)"),
        (17*17*93*677, "(3)(17**2)(31)(677)"),
        (933555431, "(7537)(123863)"),
        (342217392, "(2**4)(3)(11)(43)(15073)"),
        (35791357, "(7)(5113051)"),
        (782611830, "(2)(3**2)(5)(7**2)(11)(13)(17)(73)"),
        (775878912, "(2**8)(3**4)(17)(31)(71)"),
    ]

    def test_check_prime_factors(self):
        for tested, expected in self.test_cases:
            self.assertEqual(prime_factors(tested), expected)


if __name__ == '__main__':
    unittest.main()
