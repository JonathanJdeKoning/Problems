class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        buffer = False
        if len(nums) <= 2: return True
        for i, (a,b) in enumerate(pairwise(nums)):
            if b < a:
                if nums[:i] + nums[i+1:] == sorted(nums[:i] + nums[i+1:]): return True
                if nums[:i+1] + nums[i+2:] == sorted(nums[:i+1] + nums[i+2:]): return True
                return False
        return True