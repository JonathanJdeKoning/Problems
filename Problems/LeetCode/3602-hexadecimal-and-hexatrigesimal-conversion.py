class Solution:
    def concatHex36(self, n: int) -> str:
        def toHex(n, x):
            out = []
            while n:
                n, m = divmod(n, x)
                if m < 10:
                    out.append(str(m))
                else:
                    out.append(chr(m+55))

            return "".join(out[::-1])
        
        return toHex(n**2, 16) + toHex(n**3, 36)