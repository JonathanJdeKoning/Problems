# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = TreeNode(val=None, left=None, right=root)
        if not root: return TreeNode(val, None, None)
        prev = None
        dir = None
        while root:
            prev = root
            if root.val > val:
                root = root.left
                dir = 0
            elif root.val < val:
                root = root.right
                dir = 1
        
        if dir == 0:
            prev.left = TreeNode(val, None, None)
        else:
            prev.right = TreeNode(val, None, None)
        return dummy.right