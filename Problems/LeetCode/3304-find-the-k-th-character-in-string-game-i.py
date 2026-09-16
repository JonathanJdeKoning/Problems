class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < (k):
            new = []
            for c in word:
                new.append(chr(97+((ord(c)-97)+1)%27))
            word += "".join(new)
            print(word)
        return(word[k-1])