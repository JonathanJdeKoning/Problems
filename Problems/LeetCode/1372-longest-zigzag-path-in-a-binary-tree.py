# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        @cache
        def longestZigzag(root, direction):
            nonlocal ans
            if not root: return -1
            if not root.left and not root.right: return 0
            if direction == 1:
                best = 1 + longestZigzag(root.right, -1)
            elif direction == -1:
                best = 1 + longestZigzag(root.left, 1)                                                      
            ans = max(ans, best)
            return best

        def trav(root):
            longestZigzag(root, 1)
            longestZigzag(root, -1)

            if root.left:
                trav(root.left)
            if root.right:
                trav(root.right)

        trav(root)
        return ans