class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgs = []
        nums = sorted(nums)
        while len(nums) > 0:
            avgs.append((nums.pop() + nums.pop(0))/2)
        return len(set(avgs))
