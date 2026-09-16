class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def lcs(i, j):
            if i < 0 or j < 0: return 0
            if i ==0 and j ==0:
                return int(text1[0] == text2[0])

            if text1[i] == text2[j]:
                return lcs(i-1, j-1) + 1
            else:
                return max(lcs(i-1, j), lcs(i, j-1))

        return lcs(len(text1)-1, len(text2)-1)
