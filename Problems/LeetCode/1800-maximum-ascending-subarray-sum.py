class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx, prev, total = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            mx = max(mx, (total:=total * int(num > prev) + num))
            prev = num
        return mx
            
