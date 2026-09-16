class Solution:
    def similarPairs(self, words: List[str]) -> int:
        total = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if j >= i: continue
                if set(list(words[i])) == set(list(words[j])): total += 1
        return total