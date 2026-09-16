class Solution:
    def reverseDegree(self, s: str) -> int:
        ss = "abcdefghijklmnopqrstuvwxyz"
        mp = {}
        for i,c in enumerate(ss[::-1], start=1):
            mp[c] = i
        return sum([i*mp[c] for i, c in enumerate(s, start=1)])