# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        @cache
        def allZeros(root):
            if not root: return True
            return root.val == 0 and allZeros(root.left) and allZeros(root.right)
        if allZeros(root):
            return None

        dfs = [root]
        while dfs:
            curr = dfs.pop()
            if allZeros(curr.left):
                curr.left = None
            if allZeros(curr.right):
                curr.right = None
            if curr.left:
                dfs.append(curr.left)
            if curr.right:
                dfs.append(curr.right)
        return root


