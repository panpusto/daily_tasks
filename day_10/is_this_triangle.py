# Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built with the sides of given length and false in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).

# solution
def is_triangle(a, b, c):
    return True if a + b > c and a + c > b and b + c > a else False


# tests
import unittest

class TriangleBasicTest(unittest.TestCase):
    def test_is_triangle(self):
        self.assertEqual(is_triangle(1, 2, 2), True)
        self.assertEqual(is_triangle(4, 2, 3), True)
        self.assertEqual(is_triangle(5, 1, 5), True)
        self.assertEqual(is_triangle(2, 2, 2), True)

    def test_is_not_trangle(self):
        self.assertEqual(is_triangle(7, 2, 2), False)
        self.assertEqual(is_triangle(1, 2, 3), False)
        self.assertEqual(is_triangle(1, 3, 2), False)
        self.assertEqual(is_triangle(3, 1, 2), False)
        self.assertEqual(is_triangle(5, 1, 2), False)
        self.assertEqual(is_triangle(1, 2, 5), False)
        self.assertEqual(is_triangle(2, 5, 1), False)
        self.assertEqual(is_triangle(-1, 2, 3), False)
        self.assertEqual(is_triangle(1, -2, 3), False)
        self.assertEqual(is_triangle(1, 2, -3), False)
        self.assertEqual(is_triangle(0, 2, 3), False)

if __name__ == '__main__':
    unittest.main()
