class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2)+1))

        for i in range(1, len(word1)+1):
            new = [i]
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    new.append(dp[j-1])
                    continue
                new.append(1+min(dp[j], new[-1], dp[j-1]))
            dp = new

        return dp[-1]

            
