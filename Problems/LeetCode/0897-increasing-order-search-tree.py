# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = []

        def inOrder(root):
            if not root: return
            inOrder(root.left)
            vals.append(root.val)
            inOrder(root.right)
        inOrder(root)
        dummy = TreeNode(right=None)
        ptr = dummy
        for num in vals:
            ptr.right = TreeNode(val=num)
            ptr = ptr.right
        return dummy.right