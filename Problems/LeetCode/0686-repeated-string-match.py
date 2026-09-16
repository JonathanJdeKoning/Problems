class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        mnReps = ceil(len(b) / len(a))    
        mnStr = a*mnReps

        if b in mnStr: return mnReps
        if b in mnStr+a: return mnReps+1
        return -1    