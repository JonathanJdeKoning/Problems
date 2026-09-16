class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(nums)+1):
            out.extend(combinations(nums, i))
        return out