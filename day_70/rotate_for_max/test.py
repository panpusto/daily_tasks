import unittest
from rotate import max_rot

test_cases = [
    (38458215, 85821534),
    (195881031, 988103115),
    (896219342, 962193428),
    (69418307, 94183076)
]

class RotateForMaxBasicTests(unittest.TestCase):
    def test_count_max_num(self):
        for tested, expected in test_cases:
            self.assertEqual(max_rot(tested), expected)


if __name__ == '__main__':
    unittest.main()
