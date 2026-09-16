class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        pref = list(accumulate(nums))
        mn = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            pref[i] -= mn
            mn = min(mn, nums[i])
            
        return max(pref[:-1])