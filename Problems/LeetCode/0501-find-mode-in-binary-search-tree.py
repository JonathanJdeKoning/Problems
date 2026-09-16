# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)

        s = [root]
        out = []
        while s:
            curr = s.pop()
            count[curr.val] += 1
            if curr.left: s.append(curr.left)
            if curr.right: s.append(curr.right)
        mx = max(count.values())
        for k, v in count.items():
            if v == mx:
                out.append(k)
        return out