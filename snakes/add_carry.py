#Solution to https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Storing heads, I'm actually not sure if this is a shallow copy or not :P
        # The purpose is to not directly edit params cause that's just bad practice
        head1 = l1
        head2 = l2
        # The folloing is the sum and carry bit
        carryBit = 0
        totSum = {}
        # digCount tracks the current nth decimal place
        n = -1

        while head1 is not None or head2 is not None:
            # current sum of nth digit
            n += 1
            totSum[n] = 0
            curSum = 0
            if carryBit == 1:
                curSum += 1
            if head1 is not None:
                curSum += head1.val
                head1 = head1.next
            if head2 is not None:
                curSum += head2.val
                head2 = head2.next
            if curSum >= 10:
                curSum -= 10
                carryBit = 1
            else:
                carryBit = 0
            totSum[n] += curSum

        if carryBit == 1:
            n += 1
            totSum[n] = 0
            totSum[n] += 1

        if n is not -1:
            totSumArray = [-1] * (n + 1)
            for i in range(0, n + 1):
                totSumArray[i] = totSum[i]
            return totSumArray
        # error handling
        else:
            return -1



