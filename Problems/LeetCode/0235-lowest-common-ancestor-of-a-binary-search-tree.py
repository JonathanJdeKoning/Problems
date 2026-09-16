# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        depths = {}
        parents = {}
        def trav(root, p, d):
            depths[root] = d
            parents[root] = p

            if root.left:
                trav(root.left, root, d+1)
            if root.right:
                trav(root.right, root, d+1)

        trav(root, root, 0)


        if depths[p] < depths[q]:
            p, q = q, p
        while depths[p] != depths[q]:
            p = parents[p]
        while p!= q:
            p = parents[p]
            q = parents[q]
        return p

