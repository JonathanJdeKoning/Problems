class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            mn = heapq.heappop(nums)
            heapq.heappush(nums, -mn)
        return sum(nums)