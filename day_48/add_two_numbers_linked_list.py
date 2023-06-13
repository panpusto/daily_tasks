# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a 
# linked list.

# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not
# have leading zeros.

# solution
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        pointer = result

        while (l1 or l2 or carry):

            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0

            summation = first_num + second_num + carry

            num = summation % 10
            carry = summation // 10

            pointer.next = ListNode(num)

            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next

# tests
import unittest

class AddTwoNUmbersTests(unittest.TestCase):
    def assertLinkedListEqual(self, result, expected):
        while result and expected:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next
        self.assertIsNone(result)
        self.assertIsNone(expected)

    def test_case_1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        expected = ListNode(7)
        expected.next = ListNode(0)
        expected.next.next = ListNode(8)

        solution = Solution()
        result = solution.addTwoNumbers(l1, l2)

        self.assertLinkedListEqual(result, expected)


    def test_case_2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        expected = ListNode(0)

        solution = Solution()
        result = solution.addTwoNumbers(l1, l2)

        self.assertLinkedListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
