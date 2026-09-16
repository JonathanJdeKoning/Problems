# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        mn = 0
        mx = 0
        def trav(root, col):
            nonlocal mn
            nonlocal mx
            mn = min(col, mn)
            mx = max(col, mx)
            if root.left:
                trav(root.left, col-1)
            if root.right:
                trav(root.right, col+1)

        trav(root, 0)
        size = (mx - mn) + 1
        ans = [[] for _ in range(size)]

        q = deque([(root, abs(mn))])
        while q:
            curr, col = q.popleft()
            ans[col].append(curr.val)

            if curr.left:
                q.append((curr.left, col - 1))
            if curr.right:
                q.append((curr.right, col + 1))

        trav(root, abs(mn))
        return ans

        