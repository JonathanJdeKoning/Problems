class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        for i in range(n):
            new = s
            s += "1"+"".join(["1" if x == "0" else "0" for x in new ][::-1])
        return s[k-1]