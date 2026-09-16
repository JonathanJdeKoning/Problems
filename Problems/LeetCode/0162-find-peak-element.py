class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if (nums[0] > nums[1]): return 0
        if (nums[-1] > nums[-2]): return len(nums) - 1
        low = 1
        high = len(nums) - 2

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1

        return low
        
