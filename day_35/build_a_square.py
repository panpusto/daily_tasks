# I will give you an integer. Give me back a shape that is as long and wide as
# the integer. The integer will be a whole number between 1 and 50.

# Example
# n = 3, so I expect a 3x3 square back just like below as a string:
# +++
# +++
# +++

# solution
from itertools import repeat

def generate_shape(n):
    result = ''
    for idx, line in enumerate(repeat(n * '+', n)):
        if idx < (n - 1):
            result += f'{line}\n'
        else:
            result += line
    
    return result


# tests
import unittest

class BuildSquareBasicTests(unittest.TestCase):
    def test_generate_a_shape(self):
        self.assertEqual(generate_shape(3), '+++\n+++\n+++')
        self.assertEqual(
            generate_shape(8),
            '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++')


if __name__ == '__main__':
    unittest.main()
