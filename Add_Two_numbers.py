# Submission Details
# 1555 / 1555 test cases passed.
# Status: Accepted
# Runtime: 172 ms
# Submitted: 0 minutes ago


# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        position = 0
        result = 0
        # sentinel node
        head = ListNode(0)
        prev = head

        while l1 is not None or l2 is not None:
            if l1 is not None:
                result += l1.val
                l1 = l1.next

            if l2 is not None:
                result += l2.val
                l2 = l2.next

            node = ListNode(result % 10)
            prev.next = node
            prev = node

            result = int(result / 10)
            position += 1

        if result > 0:
            prev.next = ListNode(result)

        return head.next
