# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.
 
# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

# Constraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

# https://leetcode.com/problems/check-if-it-is-a-straight-line/


# solution
def checkStraightLine(coordinates: list[list[int]]) -> bool:
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dx = x1 - x0
    dy = y1 - y0

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if dy * (x - x1) != dx * (y - y1):
                return False
    
    return True


# tests
import unittest

class CheckStraightLineBasicTests(unittest.TestCase):
    def test_check_straight_line(self):
        self.assertEqual(
            checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]), True)
        self.assertEqual(
            checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]), False)


if __name__ == '__main__':
    unittest.main()