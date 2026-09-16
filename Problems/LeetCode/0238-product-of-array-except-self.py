class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        if nums.count(0) != 1: 
            for num in nums:
                prod *= num
        else:
            for num in nums:
                if num != 0:
                    prod *= num
        onez = nums.count(0) == 1
        for i, num in enumerate(nums):
            if not onez:
                x = num
                if num == 0:
                    x = 1 
                nums[i] = prod//x
            else:
                if num != 0:
                    nums[i] = 0
                else:
                    nums[i] = prod

        return nums
            