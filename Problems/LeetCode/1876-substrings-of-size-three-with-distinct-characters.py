class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            slc = s[i:i+3]
            if slc[0]!=slc[1] and slc[1]!= slc[2] and slc[0] !=slc[2]:
                count += 1
        return count
        