class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return sum(sorted([1]*numOnes+[0]*numZeros+[-1]*numNegOnes, reverse=True)[:k])