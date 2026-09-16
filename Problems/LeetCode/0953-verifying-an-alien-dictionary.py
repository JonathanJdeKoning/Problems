class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            good = False

            for c in range(min(len(words[i]), len(words[i+1]))):
                if words[i][c] != words[i+1][c]:
                    pair = [words[i][c],words[i+1][c]]
                    if pair != sorted(pair, key=lambda x:order.index(x)): 
                        return False
                    good = True
                    break
            if not good:
                if len(words[i]) > len(words[i+1]): return False
        return True
