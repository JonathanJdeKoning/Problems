class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        ans = 0
        z = nums.count(0)
        for i in range(len(nums)-1, -1, -1):
            if z == 0: break
            z -= 1
            if nums[i] != 0:
                ans += 1
            
        return ans
