# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants
# a diamond string from James. Since James doesn't know how to make this 
# happen, he needs your help.

# Task

# You need to return a string that looks like a diamond shape when printed
# on the screen, using asterisk (*) characters. Trailing spaces should be
# removed, and every line must be terminated with a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative, as
#  it is not possible to print a diamond of even or negative size.

# Examples

# A size 3 diamond:
#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"

# A size 5 diamond:
#   *
#  ***
# *****
#  ***
#   *
# ...that is:
# "  *\n ***\n*****\n ***\n  *\n"

# solution
def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
    result = ''
    for line in range(n):
        if line < n // 2 + 1:
            result += ' ' * (n // 2 - line) + '*' * (2 * line + 1) + '\n'
        else: 
            result += ' ' * (line - n // 2) + '*' * (2 * (n - line) - 1) + '\n'
    return result
        

# tests
import unittest

class DiamondsBasicTests(unittest.TestCase):
    def test_draw_diamond(self):
        self.assertEqual(diamond(1), '*\n')
        self.assertEqual(diamond(2), None)
        self.assertEqual(diamond(3), ' *\n***\n *\n')
        self.assertEqual(diamond(5), '  *\n ***\n*****\n ***\n  *\n')
        self.assertEqual(diamond(0), None)
        self.assertEqual(diamond(-3), None)


if __name__ == '__main__':
    unittest.main()
