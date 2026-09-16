class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace("-","")
        s = s[::-1]
        out = []
        for i in range(0,len(s),k):
            out.append(s[i:i+k][::-1])
        return "-".join(out[::-1])