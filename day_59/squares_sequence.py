# Complete the function that returns an array of length n, starting with the
# given number x and the squares of the previous number. If n is negative or
# zero, return an empty array/list.

# Examples
# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]

# solution
def squares(x: int, n: int) -> list[int]:
    if n > 1:
        seq = [x]

        for _ in range(1, n):
            seq.append(seq[-1] ** 2)

        return seq
    
    return []


# tests
import unittest

class SquaresSeqTests(unittest.TestCase):
    test_cases = [
        ((2, 5), [2, 4, 16, 256, 65536]),
        ((3, 3), [3, 9, 81]),
        ((5, 3), [5, 25, 625]),
        ((10, 4), [10, 100, 10000, 100000000]),
        ((2, 0), []),
        ((2, -4), []),
    ]

    def test_create_seq_of_squares(self):
        for tested, expected in self.test_cases:
            self.assertEqual(squares(tested[0], tested[1]), expected)


if __name__ == '__main__':
    unittest.main()
