# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# solution
def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9

# tests
import unittest

class MultiplicationBasicTests(unittest.TestCase):
    def test_simple_multiplication(self):
        self.assertEqual(simple_multiplication(2), 16)
        self.assertEqual(simple_multiplication(1), 9)
        self.assertEqual(simple_multiplication(8), 64)
        self.assertEqual(simple_multiplication(4), 32)
        self.assertEqual(simple_multiplication(5), 45)


if __name__ == '__main__':
    unittest.main()
