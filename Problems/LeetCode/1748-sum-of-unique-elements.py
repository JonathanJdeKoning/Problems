class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([int(k) for k,v in dict(Counter(nums)).items() if v == 1])