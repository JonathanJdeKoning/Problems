class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = defaultdict(int)
        for i in range(0,len(word), k):
            chunk = word[i:i+k]
            d[chunk] += 1
        
        chunks = len(word)//k
        return chunks - max(d.values())