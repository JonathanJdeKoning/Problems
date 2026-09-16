# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        sofar = root
        while q:
            sofar = q[0]
            for i in range(len(q)):
                curr = q.popleft()
                q += [node for node in [curr.left, curr.right] if node]


        return sofar.val
