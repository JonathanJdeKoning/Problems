class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        mx = max([len(x) for x in [a,b,c]])
        a = a.zfill(mx)
        b = b.zfill(mx)
        c = c.zfill(mx)
        ans = 0
        for i in range(mx):
            ax = a[i]
            bx = b[i]
            cx = c[i]

            if cx == "1":
                if "1" not in [ax,bx]:
                    ans += 1
            elif cx == "0":
                ans += [ax, bx].count("1")
        return ans