class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mn = inf
        if len(nums) == 1: return 0
        for i in range(1+(len(nums)-k)):
            a,b = nums[i],nums[i+(k-1)]
            mn = min(mn, b-a)
        return mn
        