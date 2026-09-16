class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        h = []
        ans = 0
        for num, b in zip(nums, s):
            heappush(h, -num)
            if b == "1":
                ans -= heappop(h)
        return ans
