class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i >= j or j >= k: continue
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        total += 1
        return total
