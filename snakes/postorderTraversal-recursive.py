# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Recursive solution

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # post order -> left, right, root
        postorderList = []

        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                postorderList.append(root.val)

        postorder(root)

        return postorderList