class Solution:
    def check(self, nums: List[int]) -> bool:
        bad = False
        for a,b in pairwise(nums):
            if b < a:
                if bad:
                    return False
                else:
                    bad = True
        
        if bad:
            return nums[-1] <= nums[0]
        return True