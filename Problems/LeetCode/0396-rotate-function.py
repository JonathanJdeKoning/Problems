class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        base = sum(i*num for i, num in enumerate(nums))
        ans = base
        tot = sum(nums)
        N = len(nums)
        for i in range(len(nums)-1, -1,-1):
            base += tot
            base -= N * nums[i]
            ans = max(ans, base)
        return ans
