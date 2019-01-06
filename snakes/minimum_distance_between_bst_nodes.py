# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_dist = float('inf')
        self.nodes = []

        def inorder(root, parent):
            if not root:
                return
            inorder(root.left, root)
            self.nodes.append(root.val)
            inorder(root.right, root)

        inorder(root, None)
        self.nodes.sort()
        for i in range(0, len(self.nodes) - 1):
            if self.min_dist > abs(self.nodes[i] - self.nodes[i + 1]):
                self.min_dist = abs(self.nodes[i] - self.nodes[i + 1])
        return self.min_dist