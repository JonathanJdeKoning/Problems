class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = dict(Counter(nums)).items()
        return [x[0] for x in count if x[1] == max([x[1] for x in count])][0]