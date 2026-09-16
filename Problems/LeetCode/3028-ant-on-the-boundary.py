class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        total = 0
        cnt = 0
        for num in nums:
            total += num
            if total == 0:
                cnt += 1
        return cnt
                