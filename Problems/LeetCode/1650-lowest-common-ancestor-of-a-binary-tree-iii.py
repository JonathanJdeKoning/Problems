"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        depths = {}
        root = p
        while root.parent:
            root = root.parent
        def trav(root, d):
            depths[root] = d
            if root.left:
                trav(root.left, d + 1)
            if root.right:
                trav(root.right, d + 1)
        trav(root, 0)
        if depths[p] < depths[q]:
            q, p = p, q

        while depths[p] != depths[q]:
            p = p.parent
        
        while p != q:
            p = p.parent
            q = q.parent
        return q
