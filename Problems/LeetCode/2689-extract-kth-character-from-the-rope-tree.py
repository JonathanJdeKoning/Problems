# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        s = []
        def sNode(root):
            if not root: return ""
            if not root.left and not root.right:
                return root.val
            return sNode(root.left) + sNode(root.right)
        return sNode(root)[k-1]
        