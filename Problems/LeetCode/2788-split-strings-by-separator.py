class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new = []
        for s in words:
            new += s.split(separator)
        return [x for x in new if x]