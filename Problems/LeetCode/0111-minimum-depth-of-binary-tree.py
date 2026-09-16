# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root])
        currDepth = 0
        while queue:
            currDepth += 1
            for _ in range(len(queue)):
                curr = queue.popleft()

                if not curr.left and not curr.right:
                    return currDepth
                
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
                