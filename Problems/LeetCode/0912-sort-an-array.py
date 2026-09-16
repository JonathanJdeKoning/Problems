class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        out = []
        while nums:
            out.append(heappop(nums))
        return out