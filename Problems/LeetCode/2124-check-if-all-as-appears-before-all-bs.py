class Solution:
    def checkString(self, s: str) -> bool:
        foundb = False
        for c in s:
            if c == "a" and foundb: return False
            if c == "b":
                foundb = True
        return True