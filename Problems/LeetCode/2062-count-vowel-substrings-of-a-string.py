class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        total = 0
        for i in range(len(word)):
            for j in range(i,len(word)):
                slc = word[i:j+1]
                if len(slc) <5: continue
                if len([x for x in slc if x not in "aeiou"]) != 0: continue
                if "a" in slc and "e" in slc and "i" in slc and "o" in slc and "u" in slc: total += 1
        return total
