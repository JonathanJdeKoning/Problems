class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = int(not bool(nums[i]))
                nums[i+1] = int(not bool(nums[i+1]))
                nums[i+2] = int(not bool(nums[i+2]))
                total+=1
            
        if nums[-1] ==0 or nums[-2] == 0:return -1
        return total