# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root: return 0
            return 1+ max(height(root.left), height(root.right))

        def isbal(root):
            if not root: return True
            lH = height(root.left)
            rH = height(root.right)

            return abs(lH-rH) <= 1 and isbal(root.left) and isbal(root.right)

        return isbal(root)

