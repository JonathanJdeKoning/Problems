class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        total = 0
        seen = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr = nums[:i] + nums[j+1:]
                if arr == sorted(set(arr)):
                    total += 1
        return total