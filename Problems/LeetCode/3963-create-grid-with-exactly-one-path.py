class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        G = ["."*n]
        for _ in range(m-1):
            G.append("#"*(n-1) + ".")
        return G