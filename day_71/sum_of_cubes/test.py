import unittest
from sum_of_cubes import sum_cubes

test_cases = [
    (1, 1),
    (2, 9),
    (3, 36),
    (4, 100),
    (10, 3025),
    (123, 58155876)
]

class SumCubesBasicTests(unittest.TestCase):
    def test_sum_of_cubes_in_range_n(self):
        for tested, expected in test_cases:
            self.assertEqual(sum_cubes(tested), expected)


if __name__ == '__main__':
    unittest.main()
