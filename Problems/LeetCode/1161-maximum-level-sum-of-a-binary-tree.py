# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 0
        ans = None
        bestLev  = -inf
        while q:
            level += 1
            vals = []
            for _ in range(len(q)):
                curr = q.popleft()
                vals.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if sum(vals) > bestLev:
                bestLev = sum(vals)
                ans = level
        return ans
            