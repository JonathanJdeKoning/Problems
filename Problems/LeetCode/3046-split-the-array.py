class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return len([x for x in dict(Counter(nums)).values()if x >2]) == 0