class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        poss = []
        fq = Counter(nums)
        for x in fq:
            for y in fq:
                if x >= y: continue
                if fq[x] == fq[y]: continue
                poss.append((x,y))

        poss.sort()
        if not poss: return [-1, -1]
        return [poss[0][0], poss[0][1]]
