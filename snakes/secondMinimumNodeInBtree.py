# Definition for a binary tree node.
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.smallest = float('inf')
        self.secondSmallest = float('inf')

        self.postOrder(root)
        if self.secondSmallest == float('inf'):
            return -1
        return self.secondSmallest

    def postOrder(self, root):
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        if root.val < self.smallest:
            self.secondSmallest = self.smallest
            self.smallest = root.val
        elif root.val < self.secondSmallest and root.val != self.smallest:
            self.secondSmallest = root.val
        return