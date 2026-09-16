class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        fq = Counter(n)
        mn = min(list(fq.values()))
        for k, v in sorted(fq.items()):
            if v == mn: return int(k)
