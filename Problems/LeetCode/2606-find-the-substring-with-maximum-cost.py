class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        good = set(list(chars))
        s = list(map(lambda x: vals[chars.index(x)] if x in good else ord(x)-96, list(s)))
        for i, c in enumerate(s[1:], start=1):
            s[i] = max(s[i], s[i]+s[i-1])
        return max(max(s), 0)