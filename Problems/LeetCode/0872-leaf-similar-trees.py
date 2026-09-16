# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves = []

        for root in [root1, root2]:
            rleaves = []
            q = [root]
            while q:
                for _  in range(len(q)):
                    curr = q.pop()
                    l = curr.left
                    r = curr.right
                    if not l and not r: rleaves.append(curr.val)
                    if l: q.append(l)
                    if r: q.append(r)
            leaves.append(rleaves)
        
        return leaves[0] == leaves[1]        


        
        