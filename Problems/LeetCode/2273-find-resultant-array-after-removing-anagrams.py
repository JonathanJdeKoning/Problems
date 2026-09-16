class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        while True:
            good = True
            for i in range(1, len(words)):
                a = sorted(words[i])
                b = sorted(words[i-1])
                if a == b:
                    words.pop(i)
                    good = False
                    break
            
            if good: return words
            