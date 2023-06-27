# A balanced number is a number where the sum of digits to the left of the
# middle digit(s) and the sum of digits to the right of the middle digit(s)
# are equal.

# If the number has an odd number of digits, then there is only one middle
# digit. (For example, 92645 has one middle digit, 6.) Otherwise, there are
# two middle digits. (For example, the middle digits of 1301 are 3 and 0.)

# The middle digit(s) should not be considered when determining whether a
# number is balanced or not, e.g. 413023 is a balanced number because the
# left sum and right sum are both 5.

# The task
# Given a number, find if it is balanced, and return the string "Balanced"
# or "Not Balanced" accordingly. The passed number will always be positive.

# Examples

# 7 ==> return "Balanced"
# Explanation:
# middle digit(s): 7
# sum of all digits to the left of the middle digit(s) -> 0
# sum of all digits to the right of the middle digit(s) -> 0
# 0 and 0 are equal, so it's balanced.

# 295591 ==> return "Not Balanced"
# Explanation:
# middle digit(s): 55
# sum of all digits to the left of the middle digit(s) -> 11
# sum of all digits to the right of the middle digit(s) -> 10
# 11 and 10 are not equal, so it's not balanced.

# 959 ==> return "Balanced"
# Explanation:
# middle digit(s): 5
# sum of all digits to the left of the middle digit(s) -> 9
# sum of all digits to the right of the middle digit(s) -> 9
# 9 and 9 are equal, so it's balanced.

# 27102983 ==> return "Not Balanced"
# Explanation:
# middle digit(s): 02
# sum of all digits to the left of the middle digit(s) -> 10
# sum of all digits to the right of the middle digit(s) -> 20
# 10 and 20 are not equal, so it's not balanced.

# solution
def balanced_num(number: int) -> str:
    nums = [int(num) for num in str(number)]
    left, right = 0, 0

    while len(nums) > 2:
        left += nums.pop(0)
        right += nums.pop(-1)
    
    return 'Balanced' if left == right else 'Not Balanced'


# tests
import unittest


class BalancedNumTest(unittest.TestCase):
    def test_balanced_num_odd_length(self):
        test_cases = [
            (7 , "Balanced"),
            (959, "Balanced"),
            (13, "Balanced"),
            (432, "Not Balanced"),
            (424, "Balanced"),
        ]

    def test_balanced_num_even_length(self):
        test_cases = [
            (1024, "Not Balanced"),
            (66545, "Not Balanced"),
            (295591, "Not Balanced"),
            (1230987, "Not Balanced"),
            (56239814, "Balanced"),
        ]


if __name__ == '__main__':
    unittest.main()
