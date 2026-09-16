class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return sum([val for key, val in dict(Counter(nums)).items() if val == max(list(Counter(nums).values()))])
