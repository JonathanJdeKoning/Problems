# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        q = deque([root])
        while q:
            curr = q.popleft()
            if not curr:
                continue
            q.append(curr.left)
            q.append(curr.right)
            if low <= curr.val <= high:
                total += curr.val
        return total