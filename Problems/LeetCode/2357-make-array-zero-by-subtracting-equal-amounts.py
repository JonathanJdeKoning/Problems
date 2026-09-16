class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        while True:
            if len(nums) == nums.count(0): return total
            mn = min([x for x in nums if x > 0])
            nums = list(map(lambda x:x-mn if x >0 else x, nums))
            total += 1
