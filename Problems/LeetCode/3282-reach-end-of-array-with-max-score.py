class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        mx = 0
        ans = 0
        for num in nums[:-1]:
            mx = max(num,mx)
            ans += mx
        return ans
        