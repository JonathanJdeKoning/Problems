class Solution:
    def maxValue(self, n: str, x: int) -> str:
        neg = n[0] == "-"
        if not neg:
            for i in range(len(n)):
                c = int(n[i])
                if c < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)

        else:
            for i in range(1,len(n)):
                c = int(n[i])
                if c > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)