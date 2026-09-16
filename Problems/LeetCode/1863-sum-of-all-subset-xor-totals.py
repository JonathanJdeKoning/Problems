class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for i in range(1,len(nums)+1):
            combs = combinations(nums,i)
            for comb in combs:
                total += reduce(lambda a,b: a^b, comb)
        return total