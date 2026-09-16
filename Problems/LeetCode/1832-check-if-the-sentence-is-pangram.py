class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return "".join(sorted(list(set(list(sentence))))) == "abcdefghijklmnopqrstuvwxyz"