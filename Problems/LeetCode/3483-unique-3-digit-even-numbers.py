class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = 0
        fq = Counter(digits)
        for a in range(1,10):
            if a not in fq or not fq[a]: continue
            fq[a] -= 1
            for b in range(0,10):
                if b not in fq or not fq[b]: continue
                fq[b] -= 1
                for c in range(0,10,2):
                    if c not in fq or not fq[c]: continue
                    ans += 1
                fq[b] += 1
            fq[a] += 1
        return ans