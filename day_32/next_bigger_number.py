# Create a function that takes a positive integer and returns the next bigger
# number that can be formed by rearranging its digits. 

# For example:
# 12 ==> 21
#  513 ==> 531
# 2017 ==> 2071

# If the digits can't be rearranged to form a bigger number,
# return -1 (or nil in Swift, None in Rust):
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1


# solution
def next_bigger(n):
    digits = list(str(n))

    # Find the first digit from the right that is smaller than the digit to its right
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1  # No larger number possible

    # Find the smallest digit to the right of digits[i] that is greater than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the digits to the right of i
    digits[i + 1:] = reversed(digits[i + 1:])

    # Convert the modified digits back to a number
    next_bigger_num = int(''.join(digits))
    return next_bigger_num


# tests
import unittest

class NextBiggerNumberBasicTests(unittest.TestCase):
    def test_find_next_bigger_number(self):
        self.assertEqual(next_bigger(12), 21)
        self.assertEqual(next_bigger(21), -1)
        self.assertEqual(next_bigger(513), 531)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(414), 441)
        self.assertEqual(next_bigger(144), 414)


if __name__ == '__main__':
    unittest.main()
    