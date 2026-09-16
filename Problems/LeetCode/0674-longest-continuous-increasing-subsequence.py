class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        run = 1
        prev = nums[0]

        for num in nums[1:]:
            if num > prev:
                run += 1
                ans = max(ans, run)
            else:
                run = 1
            prev = num
        return ans

