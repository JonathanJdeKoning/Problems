class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v,m="aeiou",len(s)//2        
        return len([x for x in s[:m] if x.lower()in v])==len([y for y in s[m:]if y.lower()in v])