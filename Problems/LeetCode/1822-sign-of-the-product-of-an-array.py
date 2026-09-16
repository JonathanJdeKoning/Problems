class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        return -(((len([x for x in nums if x < 0])%2)*2)-1)