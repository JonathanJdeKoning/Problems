# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mpI = {n:i for i,n in enumerate(inorder)}

        def construct(ip, jp, ii, ji):
            
            if jp < ip: return None
            root = TreeNode(preorder[ip])
            if jp-ip == 0: return root

            idx = mpI[preorder[ip]]

            leftSize = idx - ii

            root.left = construct(ip+1,leftSize+ip, ii,idx-1)
            root.right = construct(ip+leftSize+1,jp ,idx+1,ji)
            return root

        return construct(0, len(preorder)-1, 0, len(preorder)-1)
