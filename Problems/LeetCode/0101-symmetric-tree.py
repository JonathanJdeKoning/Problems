# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    level.append(None)
                    continue
                level.append(curr.val)
                
                q.append(curr.left)
                q.append(curr.right)
            if len(level) ==1:
                continue
            half = len(level)//2
            print(level)
            if level[:half] != level[half:][::-1]:
                return False
        return True
        