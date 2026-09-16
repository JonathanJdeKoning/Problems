class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negs = [x for x in nums if x < 0]
        poss = [x for x in nums if x >= 0]
        new = []
        for i in range(len(poss)):
            new.append(poss[i])
            new.append(negs[i])
        return new