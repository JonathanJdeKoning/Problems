class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        if sentence[-1][-1]!= sentence[0][0]: return False
        for i in range(len(sentence)-1):
            if sentence[i][-1] != sentence[i+1][0]: return False
        return True