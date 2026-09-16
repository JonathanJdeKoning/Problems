class Solution:
    def possibleStringCount(self, word: str) -> int:
        g = groupby(word)
        ans = 0
        for k, v in g:
            v = list(v)
            if len(v) > 1: ans += len(v)-1
        return ans +1
