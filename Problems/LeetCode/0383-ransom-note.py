class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for c in ransomNote:
            if c in magazine:
                magazine.remove(c)
            else:
                return False
        return True