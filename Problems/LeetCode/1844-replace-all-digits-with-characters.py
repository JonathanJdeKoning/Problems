class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []
        def shift(c, x):
            return chr(ord(c)+x)
        for i in range(len(s)):
            if s[i].isalpha():
                ans.append(s[i])
            else:
                ans.append(shift(s[i-1], int(s[i])))
        return "".join(ans)