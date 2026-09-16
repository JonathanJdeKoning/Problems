class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums = [-num for num in nums]
        heapify(nums)
        for _ in range(k):
            currMax = -heappop(nums)
            score += currMax
            heappush(nums, -ceil(currMax/3))
        return score