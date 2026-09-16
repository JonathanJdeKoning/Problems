# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals = []
        s =[root]
        while s:
            curr = s.pop()
            vals.append(curr.val)
            if curr.left: s.append(curr.left)
            if curr.right: s.append(curr.right)
        vals = sorted(list(set(vals)))

        if len(vals) < 2: return -1
        return vals[1]

