# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        run = 0

        def trav(root):
            nonlocal run
            if root.right:
                trav(root.right)

            run += root.val
            root.val = run

            if root.left:
                trav(root.left)
        trav(root)
        return root