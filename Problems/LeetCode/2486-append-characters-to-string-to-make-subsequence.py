class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tCount = 0 

        for c in s:
            if c == t[tCount]:
                tCount += 1
                if tCount == len(t): break

        return len(t) - tCount
