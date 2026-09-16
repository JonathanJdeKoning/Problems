class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        best = ""
        for i in range(len(s)):
            l = i
            r = i
            while True:
                if l == -1 or r == len(s): break
                if s[l] != s[r]: break
                l -= 1
                r += 1
            sub = s[(l+1):r]
            if len(sub) > mx:
                mx = len(sub)
                best = sub
            
            l=i-1
            r=i
            while True:
                if l == -1 or r == len(s): break
                if s[l] != s[r]: break
                l -= 1
                r += 1
            sub = s[(l+1):r]
            if len(sub) > mx:
                mx = len(sub)
                best = sub
                
        return "".join(best)