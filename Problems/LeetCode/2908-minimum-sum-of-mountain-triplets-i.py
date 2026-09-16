class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        mn = math.inf
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i >=j or j>= k: continue
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        mn = min(mn, sum([nums[i],nums[j],nums[k]]))
        return mn if mn != math.inf else -1