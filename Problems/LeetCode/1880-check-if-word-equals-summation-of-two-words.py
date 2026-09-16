class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstval = ""
        secondval = ""
        targetval = ""
        for c in firstWord:
            firstval += str(ord(c)-97)

        for c in secondWord:
            secondval += str(ord(c)-97)

        for c in targetWord:
            targetval += str(ord(c)-97)
        return int(firstval) + int(secondval) == int(targetval)