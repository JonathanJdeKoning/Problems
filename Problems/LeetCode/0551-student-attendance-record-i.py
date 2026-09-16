class Solution:
    def checkRecord(self, s: str) -> bool:
        if "LLL" in s: return False
        return s.count("A") <2