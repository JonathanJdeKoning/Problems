class Solution:
    def residuePrefixes(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            pref = s[:i+1]
            if len(pref)%3 == len(set(list(pref))):
                ans += 1
        return ans