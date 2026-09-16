class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev= nums[0]
        total =0
        for i, num in enumerate(nums[1:],start=1):
            if num <= prev:
                total += (prev+1)-num
                nums[i] = prev+1
            prev = nums[i]
        return total
        