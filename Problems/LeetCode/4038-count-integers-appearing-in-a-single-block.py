class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        fq = Counter()
        for k,v in groupby(nums):
            fq[k] += 1
        return list(fq.values()).count(1)
