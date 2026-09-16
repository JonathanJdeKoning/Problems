class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        cons = "bcdfghjklmnpqrstvwxyz"
        cons += cons.upper()
        valid = alphabet + "1234567890" +alphabet.upper()
        if len(word) != len([x for x in word if x in valid]): return False
        if len([x for x in word if x in "aeiouAEIOU"]) == 0: return False
        if len([x for x in word if x in cons]) == 0: return False
        return True