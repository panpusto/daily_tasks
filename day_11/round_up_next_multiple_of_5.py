# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

# Examples:
# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
# Input may be any positive or negative integer (including 0).
# You can assume that all inputs are valid integers.

# solution
def round_to_next5(n):
    return n if n % 5 == 0 else n + (5 - n % 5)

# tests
import unittest

class RoundFiveBasicTests(unittest.TestCase):
    def test_round_to_next5_func(self):
        self.assertEqual(round_to_next5(0), 0)
        self.assertEqual(round_to_next5(1), 5)
        self.assertEqual(round_to_next5(-1), 0)
        self.assertEqual(round_to_next5(5), 5)
        self.assertEqual(round_to_next5(20), 20)
        self.assertEqual(round_to_next5(39), 40)

if __name__ == '__main__':
    unittest.main()
