class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        nums = [1]*n
        
        for i in range(k):
            prev = 0
            for i, num in enumerate(nums):
                nums[i] = num + prev
                prev += num
        return nums[-1]%(10**9+7)