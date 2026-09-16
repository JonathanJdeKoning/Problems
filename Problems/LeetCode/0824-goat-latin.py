class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new = sentence.split()
        for i in range(len(new)):
            word = new[i]
            if word[0] in "aeiouAEIOU":
                newword = word+"ma"
            else:
                newword = word[1:] + word[0] +"ma"
            newword += "a"*(i+1)
            new[i] = newword
        return " ".join(new)
