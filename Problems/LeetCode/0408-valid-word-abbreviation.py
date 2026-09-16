class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        tot = 0 
        curr = 0
        for k,v in groupby(abbr, key = lambda x: x.isdigit()):
            v = list(v)
            s = "".join(v)

            if k == True:
                if s[0] == "0": return False
                curr += int(s)
            else:
                for i in range(len(s)):
                    if curr + i >= len(word): return False
                    if s[i] != word[curr + i]:
                        return False
                curr += len(s)
        return curr == len(word)