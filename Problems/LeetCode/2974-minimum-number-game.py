class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        new = []
        nums.sort()
        for i in range(0,len(nums), 2):
            new.append(nums[i+1])
            new.append(nums[i])
        return new