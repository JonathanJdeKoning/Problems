class Solution:
    def countValidPrefixes(self, s: str) -> int:
        mp = {"1": 0, "0": 0}
        ans = 0
        for c in s:
            mp[c] += 1

            if abs(mp["1"] - mp["0"]) <= 1: ans += 1
        return ans