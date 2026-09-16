# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def trav(root):
            if root.left and not root.right:
                ans.append(root.left.val)
            if root.right and not root.left:
                ans.append(root.right.val)
            if root.left:
                trav(root.left)
            if root.right:
                trav(root.right)
        trav(root)
        return ans