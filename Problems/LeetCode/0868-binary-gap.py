class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        try:
            start = b.index("1")
        except: return 0
        mx = 0
        run = 0
        for c in b[start+1:]:
            run += 1
            if c == "1":
                mx = max(run, mx)
                run = 0
        return mx
