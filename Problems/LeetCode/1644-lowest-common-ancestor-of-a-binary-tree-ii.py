# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        depth = {}
        def trav(root, p, d):
            parent[root] = p
            depth[root] = d
            if root.left: trav(root.left, root, d+ 1)
            if root.right: trav(root.right, root, d+1)
        trav(root, root, 0)
        if p not in parent or q not in parent: return None

        if depth[p] < depth[q]:
            q, p = p, q
        while depth[p] != depth[q]:
            p = parent[p]

        while q != p:
            p = parent[p]
            q = parent[q]
        return q
