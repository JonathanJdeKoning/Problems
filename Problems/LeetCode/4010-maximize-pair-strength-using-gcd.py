class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans = -math.inf
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                x, y = nums[i], nums[j]
                ans = max(ans, (x*y)/ gcd(x,y)**2)
        return int(ans)