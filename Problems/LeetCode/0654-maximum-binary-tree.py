# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        head = TreeNode()
        def buildTree(root, l, r):
            mx = -1
            idx = -1
            for i in range(l, r):
                x = nums[i]
                if x > mx:
                    mx = x
                    idx = i

            root.val = mx

            if idx-l > 0:
                root.left = TreeNode()
                buildTree(root.left,l, idx)

            if r - idx > 1:
                root.right = TreeNode()
                buildTree(root.right, idx+1, r)


        buildTree(head, 0, len(nums))
        return head
