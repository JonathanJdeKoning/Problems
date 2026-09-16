# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        depths = {}
        parents = {}
        def trav(root, par, d):
            nonlocal p
            nonlocal q
            depths[root] = d
            parents[root] = par
            if p == root.val: p = root
            if q == root.val: q = root
            if root.left:
                trav(root.left, root, d+1)
            if root.right:
                trav(root.right, root, d+1)
        trav(root, root, 0)

        origP = p
        origQ = q

        if depths[p] < depths[q]: p, q = q, p
        while depths[p] != depths[q]: p = parents[p]
        while p != q: p, q = parents[p], parents[q]

        return depths[origP] - depths[p] + depths[origQ] - depths[q]