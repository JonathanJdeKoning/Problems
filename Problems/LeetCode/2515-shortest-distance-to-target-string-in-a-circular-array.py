class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words: return -1
        startIndex += len(words)
        words = words+words+words
        pos = [i for i,x in enumerate(words) if x == target]
        mn = math.inf
        for p in pos:
            mn = min(mn, abs(p-startIndex))
        return mn
