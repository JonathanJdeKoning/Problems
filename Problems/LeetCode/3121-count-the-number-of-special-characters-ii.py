class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        import string
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        rev = word[::-1]
        total = 0
        for c in alphabet:
            firstUpper = word.find(c.upper())
            lastLower = rev.find(c)
            if firstUpper == -1 or lastLower == -1: continue
            lastLower = (len(word) - lastLower)-1
            if firstUpper < lastLower: continue
            total += 1
        return total
            
            
            
            
            
        