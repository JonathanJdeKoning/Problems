# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        @cache
        def subtreeSum(root):
            if not root: return 0
            return root.val + subtreeSum(root.left) + subtreeSum(root.right)

        fq = Counter()

        dfs = [root]
        while dfs:
            curr = dfs.pop()
            if not curr: continue

            fq[subtreeSum(curr)] += 1
            dfs.append(curr.left)
            dfs.append(curr.right)

        mx = max(list(fq.values()))
        return [k for k,v in fq.items() if v == mx]
