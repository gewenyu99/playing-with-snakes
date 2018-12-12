# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def depthFirstRob(root):
            robLeft, noRobLeft, robRight, noRobRight = 0, 0, 0, 0
            if root.left:
                robLeft, noRobLeft = depthFirstRob(root.left)
            if root.right:
                robRight, noRobRight = depthFirstRob(root.right)
            return [sum([root.val, noRobLeft, noRobRight]), sum([max(robLeft, noRobLeft), max(robRight, noRobRight)])]

        return max(depthFirstRob(root))