class Solution:
    def findValidPair(self, s: str) -> str:
        fq = Counter(s)
        for a,b in pairwise(s):
            if a == b: continue
            if fq[a] == int(a) and fq[b] == int(b):
                return a+b
        return ""