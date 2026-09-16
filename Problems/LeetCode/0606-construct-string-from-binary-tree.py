# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []

        def trav(root):
            if not root:
                ans.append(")")
                return


            ans.append(str(root.val))


            if root.right or root.left:
                ans.append("(")
                trav(root.left)
            
            if root.right:
                ans.append("(")
                trav(root.right)

            ans.append(")")
            

        trav(root)
        return "".join(ans)[:-1]