class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mn = k
        for i in range(len(blocks)-k+1):
            mn = min(mn, blocks[i:i+k].count("W"))
        return mn