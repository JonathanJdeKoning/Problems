# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        q = deque([root])

        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            if curr.val %2==0:
                if curr.left:
                    if curr.left.left:total += curr.left.left.val
                    if curr.left.right: total += curr.left.right.val
                if curr.right:
                    if curr.right.left: total += curr.right.left.val
                    if curr.right.right: total += curr.right.right.val
        return total
                        