# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        @cache
        def maxLine(root):
            if root is None: return 0
            return root.val + max(maxLine(root.left), maxLine(root.right),0)
        
        @cache
        def maxPath(root):
            if root is None: return 0
            return max(maxLine(root), root.val+maxLine(root.left)+maxLine(root.right))

        ans = -inf

        stack = [root]
        while stack:
            curr = stack.pop()
            ans = max(ans, maxPath(curr))
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return ans