# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
#
# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"

# solution
class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

# tests
import unittest

class BallBasicTests(unittest.TestCase):
    def test_create_objects(self):
        self.assertEqual(Ball().ball_type, "regular")
        self.assertEqual(Ball('super').ball_type, "super")


if __name__ == '__main__':
    unittest.main()
