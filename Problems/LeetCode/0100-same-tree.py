# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pTrav = []
        qTrav = []
        
        pStack = [p]
        while pStack:
            curr = pStack.pop()
            
            if not curr:
                pTrav.append(None)
                continue
            else:
                pTrav.append(curr.val)
            
            pStack.append(curr.left)
            pStack.append(curr.right)
        
        qStack = [q]
        while qStack:
            curr = qStack.pop()
            
            if not curr:
                qTrav.append(None)
                continue
            else:
                qTrav.append(curr.val)
            
            qStack.append(curr.left)
            qStack.append(curr.right)
            
        return pTrav == qTrav
        