# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        vals = set()
        found = False
        def trav(root):
            if not root: return
            vals.add(root.val)
            trav(root.left)
            trav(root.right)

        trav(root1)
        def trav2(root):
            nonlocal found
            if not root: return
            comp = target - root.val
            if comp in vals: found = True
            trav2(root.left)
            trav2(root.right)

        trav2(root2)
        return found