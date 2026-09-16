class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def canMake(i):
            if i == len(s): return True

            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and canMake(j):
                    return True
            return False

        return canMake(0)