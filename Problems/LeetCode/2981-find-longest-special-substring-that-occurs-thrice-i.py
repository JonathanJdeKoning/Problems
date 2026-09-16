class Solution:
    def maximumLength(self, s: str) -> int:
        import re
        chars = set(list(s))
        maxi = -1
        for i in range(1,len(s)+1):
            for c in chars:
                a = c*i
                if len(re.findall(f"(?={a})", s)) >= 3:
                    if len(a) > maxi:
                        maxi = len(a)
        return maxi
