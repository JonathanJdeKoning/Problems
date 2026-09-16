# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        totilt = 0
        if not root: return 0
        @cache
        def get_sum(root):
            if not root: return 0
            return root.val + get_sum(root.left) + get_sum(root.right)
        q = deque([root])
        while q:
            curr = q.popleft()
            totilt += abs(get_sum(curr.right) - get_sum(curr.left))
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        return totilt
