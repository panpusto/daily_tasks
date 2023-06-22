# Longest Palindrome
# Find the length of the longest substring in the given string s that is the
# same in reverse.

# As an example, if the input was “I like racecars that go fast”, the substring
# (racecar) length would be 7.

# If the length of the input string is 0, the return value must be 0.

# Example:
# "a" -> 1 
# "aab" -> 2  
# "abcde" -> 1
# "zzbaabcd" -> 4
# "" -> 0
###############################################################################

# solution
def longest_palindrome(s):
    max_len = 0

    for left in range(len(s)):
        for right in range(len(s), left, -1):
            if s[left:right] == s[left:right][::-1]:
                max_len = max(max_len, right - left)
    
    return max_len


# tests
import unittest


class PalindromeTests(unittest.TestCase):
    def test_find_length_of_longest_palindrome(self):
        test_cases = [
            ("a", 1),
            ("aa", 2),
            ("baa", 2),
            ("aab", 2),
            ("abcdefghba", 1),
            ("baablkj12345432133d", 9)
        ]

        for tested_val, expected_val in test_cases:
            self.assertEqual(longest_palindrome(tested_val), expected_val)


if __name__ == '__main__':
    unittest.main()
