class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        o = len([x for x in nums if x%2==1])
        e = len(nums) - o
        return ([0]*e) + ([1]*o)