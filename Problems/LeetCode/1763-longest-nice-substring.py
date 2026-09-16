class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        curr = ""
        for i in range(len(s)-1):
            for j in range(i+2,len(s)+1):
                slc = s[i:j]
                bad = False
                for c in slc:
                    if c.islower():
                        if c.upper() not in slc:
                            bad = True
                            break
                    elif c.isupper():
                        if c.lower() not in slc:
                            bad = True
                            break
                if not bad:
                    if len(slc) > len(curr):
                        curr = "".join(slc)
        return curr

