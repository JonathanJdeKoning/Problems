import operator
class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        P = list(accumulate(nums, initial=0))
        S = list(accumulate(nums[::-1], lambda a,b: (a*b) if (a*b)<= P[-1] else P[-1]+1, initial=1))[::-1]

        for i in range(len(nums)):
            leftSum = P[i]
            rightMul = S[i+1]
            if leftSum == rightMul:
                return i
        return -1