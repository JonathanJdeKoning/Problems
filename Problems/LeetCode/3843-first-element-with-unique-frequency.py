class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        fq = Counter(nums)
        fqfq = Counter(list(fq.values()))
        for num in nums:
            if fqfq[fq[num]] == 1: return num
        return -1