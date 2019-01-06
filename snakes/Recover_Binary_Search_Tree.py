# https://leetcode.com/problems/recover-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        If constant space, do the min max thing without "past vals"
        """
        past_vals = []
        elems = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            past_vals.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(0, len(past_vals) - 1):
            if not past_vals[i] < past_vals[i + 1]:
                elems.extend([past_vals[i], past_vals[i + 1]])

        # you'd swap the largest and smallest values
        max_val = max(elems)
        min_val = min(elems)

        def swap(root):
            if not root:
                return
            swap(root.left)
            if root.val == max_val:
                root.val = min_val
            elif root.val == min_val:
                root.val = max_val
            swap(root.right)

        swap(root)
