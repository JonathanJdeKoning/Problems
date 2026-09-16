class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for c in s:
            left = s.index(c)
            right = len(s) - s[::-1].index(c) - 1
            if (right - left) - 1 != distance[ord(c)-97]:
                return False
        return True