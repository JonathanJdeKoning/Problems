class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        last1 = -1
        last2 = -1
        ans = inf
        for i, word in enumerate(wordsDict):
            if word == word1:
                last1 = i
            elif word == word2:
                last2 = i

            if last1 != -1 and last2 != -1:
                ans = min(ans, abs(last1 - last2))
        return ans