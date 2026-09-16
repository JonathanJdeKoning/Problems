# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def trav(root, mx):
            nonlocal ans
            
            mx = max(mx, root.val)
            if root.val == mx: ans += 1

            if root.left:  trav(root.left, mx)
            if root.right: trav(root.right, mx)
        trav(root, -inf)
        return ans

