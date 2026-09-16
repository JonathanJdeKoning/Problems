# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        parent = {}
        depths = {}

        def trav(root, p, d):
            parent[root] = p
            depths[root] = d
            if root.left: trav(root.left, root, d+1)
            if root.right: trav(root.right, root, d+1)
        trav(root, root, 0)
        minDepth = min([depths[n] for n in nodes])
        print(minDepth)
        for i in range(len(nodes)):
            while depths[nodes[i]] != minDepth:
                nodes[i] = parent[nodes[i]]
        def checkAllSame():
            base = nodes[0]
            for node in nodes:
                if node != base: return False
            return True

        while not checkAllSame():
            for i in range(len(nodes)):
                nodes[i] = parent[nodes[i]]
        return nodes[0]

        
