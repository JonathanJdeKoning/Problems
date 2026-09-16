# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        val = root.val

        while q:
            n = q.popleft()
            if n.val != val:
                return False
            
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return True

