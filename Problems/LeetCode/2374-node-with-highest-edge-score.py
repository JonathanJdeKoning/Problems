class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        mp = defaultdict(int)
        for i, num in enumerate(edges):
            mp[num] += i


        best = 0
        bestidx = 0
        for i in range(len(edges)):
            if mp[i] > best:
                best = mp[i]
                bestidx = i
        return bestidx
