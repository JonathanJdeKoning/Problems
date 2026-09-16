class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, num in enumerate(sorted(nums)):
            if num == target:
                res.append(i)
        return res