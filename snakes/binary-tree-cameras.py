# https://leetcode.com/problems/binary-tree-cameras/
class Solution:
    def minCameraCover(self, root):
        """
        Very similar to the idea of house robbers
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 1

        def modified_dfs(root):
            left, right, noleft, noright, mustleft, mustright = float('inf'), float('inf'), 0, 0, 0, 0
            if root.left:
                left, noleft, mustleft = modified_dfs(root.left)
            if root.right:
                right, noright, mustright = modified_dfs(root.right)

            return [sum([1, min(left, noleft, mustleft), min(right, noright, mustright)]),
                    min(left + right, noleft + right, noright + left),
                    noleft + noright]

        a, b, c = (modified_dfs(root))
        return min(a, b)