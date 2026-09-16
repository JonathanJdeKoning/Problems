class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for c in s:
            if c == "i":
                ans = list(reversed(ans))
            else:
                ans.append(c)
        return "".join(ans)