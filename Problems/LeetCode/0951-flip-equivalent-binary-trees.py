# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        def trav(root):
            if not root: return
            if not root.left and not root.right:
                return
            if not root.left:
                root.left, root.right = root.right, root.left
            if root.left and root.right:
                if root.left.val > root.right.val:
                    root.left, root.right = root.right, root.left

            trav(root.left)
            trav(root.right)
        trav(root1)
        trav(root2)
        walkArr1 = []
        walkArr2 = []

        def walk1(root):
            if not root:
                walkArr1.append(None)
                return
            
            walkArr1.append(root.val)
            walk1(root.left)
            walk1(root.right)

        def walk2(root):
            if not root:
                walkArr2.append(None)
                return
            
            walkArr2.append(root.val)
            walk2(root.left)
            walk2(root.right)
        walk1(root1)
        walk2(root2)
        print(walkArr1)
        print(walkArr2)
        return walkArr1 == walkArr2
