# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font
# for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number
# of rows:

# string convert(string s, int numRows);


# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"

# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"

# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


# solution
def convert(s: str, num_rows: int) -> str:
    if s is None and num_rows <= 0:
        return ""
    
    if num_rows == 1:
        return s
    
    result = ''
    step = 2 * num_rows - 2

    for i in range(0, num_rows):
        for j in range(i, len(s), step):
            result += s[j]
            if i != 0 and i != num_rows - 1 and (j + step - 2 * i) < len(s):
                result += s[j + step - 2 * i]

    return result


# tests
import unittest

class ZigZagConvertTests(unittest.TestCase):
    test_cases = [
        (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
        (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
        (("PAYPALISHIRING", 1), "PAYPALISHIRING"),
    ]

    def test_convert(self):
        for tested, expected in self.test_cases:
            self.assertEqual(convert(tested[0], tested[1]), expected)

    


if __name__ == '__main__':
    unittest.main()
