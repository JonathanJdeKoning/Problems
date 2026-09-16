class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        uniq = set(s)
        mx = {}
        mn = {c:s.index(c) for c in uniq}
        for i, c in enumerate(s):
            mx[c] = i
        ans = -1
        for c in uniq:
            ans = max(ans, (mx[c] - mn[c]) - 1)
        return ans
