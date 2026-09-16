class Solution:
    def countLetters(self, s: str) -> int:
        ans = 0
        g = groupby(s)

        for k,v in g:
            l = len(list(v))
            ans += (l*(l+1)) // 2
        return ans