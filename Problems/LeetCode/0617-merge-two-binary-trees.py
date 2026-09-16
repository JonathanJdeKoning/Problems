# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        old = root1
        if not root1: return root2
        if not root2: return root1
        def dfs(root1, root2):
            if root2: root1.val += root2.val

            if root1.left and root2.left:
                dfs(root1.left, root2.left)
            
            if root1.right and root2.right:
                dfs(root1.right, root2.right)

            if root2.left and not root1.left:
                root1.left = root2.left

            if root2.right and not root1.right:
                root1.right = root2.right

        dfs(root1, root2)
        return old

        