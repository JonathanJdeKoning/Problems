class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if x==y and i < j:
                    total += 1
        return total