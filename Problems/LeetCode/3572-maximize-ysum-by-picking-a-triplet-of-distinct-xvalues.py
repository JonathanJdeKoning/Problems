class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mp = defaultdict(int)
        for i in range(len(x)):
            mp[x[i]] = max(mp[x[i]], y[i])

        if len(mp) < 3: return -1

        v = list(mp.values())
        v.sort()
        return v.pop() + v.pop()  + v.pop()