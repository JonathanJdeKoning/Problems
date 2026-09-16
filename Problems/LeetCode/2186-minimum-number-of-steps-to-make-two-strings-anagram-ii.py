class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sFQ = Counter(s)
        tFQ = Counter(t)
        A = set(list(sFQ.keys()) + list(tFQ.keys()))
        ans = 0
        for c in A:
            ans += max(sFQ[c], tFQ[c]) - min(sFQ[c], tFQ[c])
        return ans
