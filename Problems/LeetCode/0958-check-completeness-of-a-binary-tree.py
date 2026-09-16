# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        v = 1
        q = deque([root])
        flag = False
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    flag = True 
                    continue
                else:
                    if flag: return False

                q.append(curr.left)
                q.append(curr.right)
                v += 1
        return True