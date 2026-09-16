class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        mx = 0
        a = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(a)+1):
            for j in range(i+1, len(a)+1):
                chk = a[i:j]
                if chk in s:
                    mx = max(mx, len(chk))
        return mx