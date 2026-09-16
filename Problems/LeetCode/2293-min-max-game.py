class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while True:
            if len(nums) == 1: return nums[0]
            newNums = [None]*(len(nums)//2)

            for i, x in enumerate(newNums):
                if i%2==0:
                    newNums[i] = min(nums[2*i], nums[2*i+1])
                else:
                    newNums[i] = max(nums[2*i], nums[2*i+1])
            nums = newNums
