# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        ans = 0

        def exhaust(root, tot=0):
            nonlocal ans
            tot += root.val
            if tot == targetSum:
                ans += 1
            if root.left:
                exhaust(root.left, tot)
            if root.right:
                exhaust(root.right, tot)
            
            

        dfs = [root]

        while dfs:
            curr = dfs.pop()
            exhaust(curr)

            if curr.left: dfs.append(curr.left)
            if curr.right: dfs.append(curr.right)
        return ans