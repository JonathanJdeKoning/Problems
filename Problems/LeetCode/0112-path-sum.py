# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def isLeaf(node):
            return not node.left and not node.right

        stack = [(root, targetSum)]

        while stack:
            currNode, currTarget = stack.pop()

            if not currNode: continue

            if currNode.val == currTarget and isLeaf(currNode):
                return True

            subTarget = currTarget - currNode.val
            stack.append((currNode.right, subTarget))
            stack.append((currNode.left, subTarget))
        return False