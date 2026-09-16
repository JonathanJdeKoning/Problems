class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return bool([x for x in s if x in "aeiou"])