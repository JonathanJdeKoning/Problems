# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return None
        order = []
        def preorder(root):
            order.append(root)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)
            root.left = None
            root.right = None
        preorder(root)
        for a,b in pairwise(order):
            a.right = b
        return order[0]
        