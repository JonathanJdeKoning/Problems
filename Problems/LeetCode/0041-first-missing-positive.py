class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        for i in range(1,100002):
            if i not in count: return i