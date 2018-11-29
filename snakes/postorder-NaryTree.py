# https://leetcode.com/problems/n-ary-tree-postorder-traversal/ < this one!

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# TODO: iter solution, but it should be very similar to bintry postorder in logic

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        postorderList = []

        if not root:
            return []
        if not root.children:
            return [root.val]

        def recur(root):
            for child in root.children:
                recur(child)
            postorderList.append(root.val)

        recur(root)
        return postorderList
