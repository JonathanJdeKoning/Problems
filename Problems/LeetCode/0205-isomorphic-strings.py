class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        used = set()
        for a, b in zip(s, t):
            if a in mp and mp[a] == b: continue
            if a in mp: return False
            if b in used: return False
            mp[a] = b
            used.add(b)
        return True
    


