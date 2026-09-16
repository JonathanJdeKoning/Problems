# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r,s):
            if r is None and s is not None: return false
            if s is None and r is not None: return false
            if r is None and s is None: return True

            if r.val != s.val: return False
            if r.left and not s.left: return False
            if r.right and not s.right: return False
            if s.left and not r.left: return False
            if s.right and not r.right: return False

            return isSame(r.left, s.left) and isSame(r.right, s.right)

        
        dfs = [root]
        while dfs:
            curr = dfs.pop()
            if isSame(curr, subRoot): return True
            if curr.left: dfs.append(curr.left)
            if curr.right: dfs.append(curr.right)
        return False