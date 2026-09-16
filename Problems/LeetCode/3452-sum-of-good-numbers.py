class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, num in enumerate(nums):
            l = i-k
            r = i+k
            if l in range(0,len(nums)):
                if num <= nums[l]: continue
            if r in range(0, len(nums)):
                if num <= nums[r]: continue
            ans += num
        return ans