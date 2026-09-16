class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in s: continue
            start = s.index(c)
            end = (len(s)-s[::-1].index(c))-1
            ans += len(set(s[start+1:end]))

        return ans