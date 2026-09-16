class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        q = [root]
        while q:
            curr = q.pop()
            if k-curr.val in nums: return True
            nums.add(curr.val)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        return False
