class Solution:
    def sortSentence(self, s: str) -> str:
        new = sorted(s.split(), key= lambda item:item[-1])
        final = ""
        for item in new:
            final += item[:-1] + " "
        return final[:-1]