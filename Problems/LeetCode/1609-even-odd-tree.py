# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def strict(A):
            for a,b in pairwise(A):
                if b<=a: return False
            return True

        q = deque([root])
        currLevel = 0

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            if currLevel % 2 == 0:
                if len([x for x in level if x%2==0]): return False
                if not strict(level): return False
            else:
                if len([x for x in level if x%2==1]): return False
                if not strict(level[::-1]): return False
            currLevel += 1
        return True
                