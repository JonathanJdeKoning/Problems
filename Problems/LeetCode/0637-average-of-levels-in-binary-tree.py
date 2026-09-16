# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr: level.append(curr.val)
                else: continue
                q.append(curr.left)
                q.append(curr.right)

            if len(level) != 0:
                ans.append(sum(level) / len(level))
        return ans