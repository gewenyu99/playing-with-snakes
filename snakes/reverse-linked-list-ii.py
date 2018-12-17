# https://leetcode.com/problems/reverse-linked-list-ii/

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p = head
        detachedHead = None
        detachedTail = None
        breakNode = None
        for i in range(1, m):
            breakNode = p
            p = p.next

        # p is the mth element here
        prevElement = None
        for i in range(0, n - m + 1):
            nextElem = p.next
            if i == 0:
                detachedTail = p
            else:
                p.next = prevElement
            prevElement = p
            p = nextElem
        detachedHead = prevElement
        detachedTail.next = p
        if breakNode:
            breakNode.next = detachedHead
        else:
            head = detachedHead

        return head


def printLL(h):
    while h:
        print(h.val)
        h = h.next
