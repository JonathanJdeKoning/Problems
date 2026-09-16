class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        fq = Counter(str(n))
        return sum(int(k)* d for k,d in fq.items())