# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = 0
        @cache
        def mxDepth(root):
            nonlocal mx
            if not root: return 0
            mx = max(mxDepth(root.left) + mxDepth(root.right), mx)
            return 1+ max(mxDepth(root.left), mxDepth(root.right))

        mxDepth(root)
        return mx
        
        
