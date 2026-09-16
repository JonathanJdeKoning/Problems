# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        seen = []
        q = deque([root])
        while q:
            curr = q.popleft()
            seen.append(curr.val)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        seen.sort()
        mn = inf
        for i in range(len(seen)-1):
            dist = abs(seen[i] - seen[i+1])
            mn = min(mn, dist)
        return mn
