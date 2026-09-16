# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        ans = []

        for root in [root1, root2]:
            if not root: continue
            s = [root]
            while s:
                curr = s.pop()

                ans.append(curr.val)
                if curr.left: s.append(curr.left)
                if curr.right: s.append(curr.right)
        return sorted(ans)
