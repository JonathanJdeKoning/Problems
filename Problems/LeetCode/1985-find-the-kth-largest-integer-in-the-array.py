class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(x) for x in nums]
        heapq.heapify(nums)
        return str(heapq.nlargest(k, nums)[-1])