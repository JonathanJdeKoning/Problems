# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def subtreeInfo(node):
            nonlocal ans
            if not node: return (0,0)
            leftInfo = subtreeInfo(node.left)
            rightInfo = subtreeInfo(node.right)
            totalInfo = (leftInfo[0] + rightInfo[0] + 1, leftInfo[1] + rightInfo[1] + node.val)

            if totalInfo[1] // totalInfo[0] == node.val: ans += 1
            return totalInfo



        subtreeInfo(root)
        return ans