class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mp = {c:i for i, c in enumerate(keyboard)}
        prev = 0
        ans = 0
        for c in word:
            d = abs(mp[c] - prev)
            ans += d
            prev = mp[c]
        return ans