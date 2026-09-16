# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mini, maxi):
            if not node:
                return maxi - mini
            
            mini = min(mini, node.val)
            maxi = max(maxi, node.val)
            
            left = dfs(node.left, mini, maxi)
            right = dfs(node.right, mini, maxi)
            
            return max(left, right)
        
        return dfs(root, root.val, root.val)
