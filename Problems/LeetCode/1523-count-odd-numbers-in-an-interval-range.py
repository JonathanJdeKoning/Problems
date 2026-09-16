class Solution:
    def countOdds(self, low: int, high: int) -> int:
            numnums = (high-low)+1
            if numnums%2 != 0:
                if low%2!=0:
                    return (numnums//2)+1
            return numnums//2