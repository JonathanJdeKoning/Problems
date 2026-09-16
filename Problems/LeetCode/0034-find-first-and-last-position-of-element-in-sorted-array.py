class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def startCond(idx):
            return nums[idx] >= target

        def endCond(idx):
            return nums[idx] > target
        
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if startCond(mid):
                high = mid
            else:
                low = mid + 1
        start = low

        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if endCond(mid):
                high = mid
            else:
                low = mid + 1
        end = low - 1
        if end == -1:
            return [-1,-1]

        return [start, end]

        