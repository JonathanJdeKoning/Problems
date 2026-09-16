# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def maximumDepth(root):
            if not root: return 0

            maxDepthLeft = maximumDepth(root.left)
            maxDepthRight = maximumDepth(root.right)

            return 1 + max(maxDepthLeft, maxDepthRight)

        return maximumDepth(root)