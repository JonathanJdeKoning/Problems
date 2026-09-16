class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) == len(s2): return s1==s2
        if len(s1) > len(s2):
            for i in range(len(s1)):
                for j in range(i, len(s1)):
                    chk = s1[:i] + s1[j+1:]

                    if chk == s2: return True
            return False

        elif len(s2) > len(s1):
            for i in range(len(s2)):
                for j in range(i, len(s2)):
                    chk = s2[:i] + s2[j+1:]

                    if chk == s1: return True
            return False
