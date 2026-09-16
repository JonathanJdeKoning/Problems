# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -inf
        def inorder(node):
            nonlocal prev
            if not node: return
        
            inorder(node.left)
            if node.val <= prev: prev = inf
            prev = max(node.val, prev)
            inorder(node.right)

        inorder(root)
        return prev != inf