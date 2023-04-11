# Find the total sum of internal angles (in degrees) in an n-sided simple polygon. N will be greater than 2.

# solution
def angle(n):
    return (n - 2) * 180

# tests
import unittest
class AngleBasicTests(unittest.TestCase):
    def test_angle_function(self):
        self.assertEqual(angle(3), 180)
        self.assertEqual(angle(4), 360)


if __name__ == '__main__':
    unittest.main()
