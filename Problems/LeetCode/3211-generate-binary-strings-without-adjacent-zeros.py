class Solution:
    def validStrings(self, n: int) -> List[str]:
        out = []
        mx = int("1"*n,2)
        for i in range(0,mx+1):
            s = bin(i)[2:].zfill(n)
            if "00" in s: continue
            out.append(s)
        return out