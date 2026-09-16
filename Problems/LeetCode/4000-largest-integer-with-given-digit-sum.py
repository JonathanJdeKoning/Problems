class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        base = [0]*n
        i = 0
        while s and i < n:
            take = min(s, 9)
            s -= take
            base[i] = take
            i+= 1
        if s: return -1
        return int("".join(map(str, base)))