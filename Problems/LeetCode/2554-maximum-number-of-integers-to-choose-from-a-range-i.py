class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        curr = 0
        ans = 0
        for i in range(1, n+1):
            if i in banned: continue
            if curr + i <= maxSum:
                curr += i
                ans += 1
            else: break
        return ans