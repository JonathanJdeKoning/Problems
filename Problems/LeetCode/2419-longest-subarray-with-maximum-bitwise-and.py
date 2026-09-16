class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = 1
        for k, v in groupby(nums):
            if k == mx:
                ans = max(ans, len(list(v)))
        return ans