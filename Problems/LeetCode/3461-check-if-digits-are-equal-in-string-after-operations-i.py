class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2: 
            s = "".join(map(str, [(int(a) + int(b))%10 for a,b in pairwise(s)]))
        return s[0] == s[1]