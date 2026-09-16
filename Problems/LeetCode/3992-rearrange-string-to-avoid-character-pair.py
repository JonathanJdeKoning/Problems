class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        fq = Counter(s)
        base = y*fq[y] + x*fq[x]

        del fq[y]
        del fq[x]
        for k, v in fq.items():
            base += k*v
        return base