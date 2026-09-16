class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while nums != sorted(nums):
            ans += 1
            mnsum = min([a+b for a,b in pairwise(nums)])
            
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] == mnsum:
                    nums = nums[:i] + [mnsum] + nums[i+2:]
                    break
        return ans