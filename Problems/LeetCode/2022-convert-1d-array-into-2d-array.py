class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n: return []

        new = []
        for i in range(0, len(original),n):
            new.append(original[i:i+n])
        return new
