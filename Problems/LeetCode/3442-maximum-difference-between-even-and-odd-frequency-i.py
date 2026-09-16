class Solution:
    def maxDifference(self, s: str) -> int:
        fq = Counter(s)
        fqs = list(fq.values())
        eve = [x for x in fqs if x%2==0]
        odd = [x for x in fqs if x%2==1]
        return max(odd) - min(eve)