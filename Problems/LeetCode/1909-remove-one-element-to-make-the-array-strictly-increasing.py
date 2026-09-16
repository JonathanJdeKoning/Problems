class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if nums == sorted(nums) and len(Counter(nums)) == len(nums): return True
        for i in range(len(nums)):
            x = nums[:i]+nums[i+1:]
            if x == sorted(x):
                if len(Counter(x)) == len(x): return True
        return False

