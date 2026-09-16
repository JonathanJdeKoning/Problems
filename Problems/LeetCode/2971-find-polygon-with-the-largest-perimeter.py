class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        tot = nums[0] + nums[1]
        ans = -1
        for num in nums[2:]:
            if num < tot:
                ans = max(ans, tot+num)
            tot += num
        return ans