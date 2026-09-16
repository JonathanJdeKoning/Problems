class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        totalO = sum(nums[1::2])
        totalE = sum(nums[0::2])

        preO = 0
        preE = 0
        for i, num in enumerate(nums):
            postO = totalO - preO
            postE = totalE - preE
            if i%2==0: postE -= num
            else: postO -= num

            if (postE + preO) == (postO + preE): ans += 1
            
            
            if i%2==0: preE += num
            else: preO += num
        return ans
