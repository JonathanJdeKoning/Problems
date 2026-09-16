class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        nums.sort()
        while nums:
            avg.append((nums[0]+nums[-1])/2)
            nums = nums[1:-1]
        return min(avg)