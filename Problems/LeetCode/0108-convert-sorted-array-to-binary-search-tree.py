# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def createBST(i,j):
            if j < i: return None
            if i == j:
                return TreeNode(nums[i])
            
            mid = (i+j) // 2

            root = TreeNode(nums[mid])
            root.left = createBST(i, mid-1)
            root.right = createBST(mid+1, j)
            return root
        return createBST(0, len(nums) - 1)