class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sing = [x for x in nums if x <10]
        doub = [x for x in nums if x >=10]

        return sum(sing)!=sum(doub)        