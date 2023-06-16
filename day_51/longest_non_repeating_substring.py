# Given a string s, find the length of the longest
# substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence
# and not a substring.
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# solution
def length_of_longest_substring(s: str) -> int:
    start = 0
    end = 0
    max_len = 0
    checked = set()

    while end < len(s):
        if s[end] not in checked:
            checked.add(s[end])
            current_max = end - start + 1
            max_len = max(max_len, current_max)
            end += 1
        else:
            checked.remove(s[start])
            start += 1
    return max_len


# tests
import unittest

class LongestSubstringTests(unittest.TestCase):
    def test_longest_substring(self):
        test_cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3)
        ]

        for string, result in test_cases:
            self.assertEqual(length_of_longest_substring(string), result)


if __name__ == '__main__':
    unittest.main()
