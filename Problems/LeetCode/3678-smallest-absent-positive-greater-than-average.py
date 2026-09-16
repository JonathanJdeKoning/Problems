class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        for i in range(max(floor(avg)+1, 1), 1000000):
            if i not in nums: 
                return i