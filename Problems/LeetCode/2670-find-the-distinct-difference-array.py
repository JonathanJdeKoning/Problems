class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        new = []
        for i in range(len(nums)):
            back = nums[:i+1]
            forw = nums[i+1:]
            new.append(len(set(back)) - len(set(forw)))
        return new