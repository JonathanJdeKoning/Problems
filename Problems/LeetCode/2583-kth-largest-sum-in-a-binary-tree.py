class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        q = deque([root])
        while q:
            level = 0
            for _ in range(len(q)):
                curr = q.popleft()
                level += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            sums.append(level)

        if len(sums) < k: return -1
        return sorted(sums, reverse=True)[k-1]