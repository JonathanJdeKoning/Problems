class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        total = 0
        seen = set()
        for c in word:
            if c.islower() and c not in seen: 
                if c.upper() in word:
                    total += 1
                    seen.add(c.lower())
                    seen.add(c.upper())
            elif c.isupper() and c not in seen:
                if c.lower() in word:
                    seen.add(c.upper())
                    seen.add(c.lower())

                    total += 1
        return total