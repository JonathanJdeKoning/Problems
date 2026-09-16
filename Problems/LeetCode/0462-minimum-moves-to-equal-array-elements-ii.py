class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = statistics.median(nums)

        ans = sum([abs(median - x) for x in nums])
        return int(ans)