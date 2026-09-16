class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lowers = [x for x in word if x.islower()]
        if len(lowers) in [0,len(word)]: return True
        return word[0].isupper() and len([x for x in word[1:] if x.isupper()]) == 0