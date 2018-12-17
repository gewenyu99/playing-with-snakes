# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Use the Doubly linked list in cache is we want faster performance in the future, even with deletes and inserts

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cache = Cache()

        def postorder(root):
            if root:
                l = postorder(root.left)
                if l != None:
                    return l
                cache.elemCount += 1
                if cache.elemCount == k:
                    return root.val
                r = postorder(root.right)
                if r != None:
                    return r
                return None

        return (postorder(root))


class Cache:
    def __init__(self):
        self.elemCount = 0
        self.DLLroot = DLL(None)
        self.DLLtail = self.DLLroot

    def addRecord(self, val):
        self.DLLtail.next = DLL(val)
        self.DLLtail.next.prev = self.DLLtail
        self.DLLtail = self.DLLtail.next


class DLL:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

    def add(self, val):
        if self.val == None:
            self.val = val
            return
        p = self
        while p.next:
            p = p.next
        p.next = DLL(val)
        p.next.prev = p
        return
