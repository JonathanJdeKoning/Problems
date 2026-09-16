# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = 0
        def sizeAndSumSubtree(root):
            nonlocal ans
            if not root: return (0,0)
            rootSize = 1
            rootSum = root.val
            
            leftSize, leftSum = sizeAndSumSubtree(root.left)
            rightSize, rightSum = sizeAndSumSubtree(root.right)

            rootSize += leftSize + rightSize
            rootSum += leftSum + rightSum

            avg = rootSum / rootSize
            ans = max(ans, avg)
            return (rootSize, rootSum)
        sizeAndSumSubtree(root)
        return ans

