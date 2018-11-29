# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # post order -> left, right, root

        # 1. Iteratively, we go try to go left til we can't
        # 2. we go right and check for 1 til we can't
        # 3. we print cur val
        # we go back to one

        postorderList = []

        if not root:
            return []

        prevNodes = []
        if root.left:
            prevNodes.append(root)
            curNode = root.left
        elif root.right:
            prevNodes.append(root)
            curNode = root.right
        else:
            return [root.val]

        while curNode:
            print(curNode.val)
            if curNode.left:
                prevNodes.append(curNode)
                curNode = curNode.left
            elif curNode.right:
                prevNodes.append(curNode)
                curNode = curNode.right
            else:
                postorderList.append(curNode.val)
                if prevNodes:
                    curNode = prevNodes.pop()
                    if curNode.left:
                        curNode.left = None
                    elif curNode.right:
                        curNode.right = None
                else:
                    break

        return postorderList