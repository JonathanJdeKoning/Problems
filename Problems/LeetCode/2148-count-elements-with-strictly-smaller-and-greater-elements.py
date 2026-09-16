class Solution:
    def countElements(self, nums: List[int]) -> int:
        total = 0

        for i, num in enumerate(nums):
            rest = nums[:i] + nums[i+1:]
            if len(rest) ==0 : return 0
            if max(rest) > num and min(rest) < num:
                total += 1
        return total