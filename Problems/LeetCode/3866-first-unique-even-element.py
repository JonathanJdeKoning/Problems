class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        fq = Counter(nums)

        for i, n in enumerate(nums):
            if fq[n] == 1 and n%2==0: return n
        return -1