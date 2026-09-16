class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []

        for i in range(len(text)):
            for j in range(i+1, len(text)+1):
                if text[i:j] in words:
                    ans.append([i, j-1])
        return ans