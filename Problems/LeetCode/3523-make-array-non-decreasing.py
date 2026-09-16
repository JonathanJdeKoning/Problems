class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        mx = nums[0]
        ans = 1
        for num in nums[1:]:
            if num >= mx:
                ans += 1
                mx = num
        return ans