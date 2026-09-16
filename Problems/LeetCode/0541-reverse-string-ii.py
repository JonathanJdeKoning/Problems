class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        out = []
        for i in range(0,len(s),k*2):
            out.append(s[i:i+2*k][:k][::-1] + s[i:i+2*k][k:])
        return "".join(out)