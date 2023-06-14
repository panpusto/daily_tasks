# Given the root of a Binary Search Tree (BST), return the minimum absolute
# difference between the values of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:
# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# solution
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        current = root
        prev_val = None
        min_diff = float('inf')

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()

            if prev_val is not None:
                min_diff = min(min_diff, abs(current.val - prev_val))
            
            prev_val = current.val
            current = current.right
        
        return min_diff

# tests
import unittest

class MinimumDiffTests(unittest.TestCase):
    def test_case_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        solution = Solution()
        result = solution.getMinimumDifference(root)

        self.assertEqual(result, 1)

    def test_case_2(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(48)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(49)

        solution = Solution()
        result = solution.getMinimumDifference(root)

        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
