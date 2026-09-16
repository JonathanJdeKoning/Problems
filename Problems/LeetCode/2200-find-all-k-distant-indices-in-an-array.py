class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        keyIndices = []

        for idx, val in enumerate(nums):
            if key == val:
                keyIndices.append(idx)
        
        for idx, val in enumerate(nums):
            for index in keyIndices:
                if abs(idx - index) <= k:
                    res.append(idx)
                    break
        
        return res