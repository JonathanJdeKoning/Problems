class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(map(len, [x.split() for x in sentences]))
