class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        bad = []
        if len(s)!= len(goal): return False
        for i in range(len(s)):
            if s[i]!=goal[i]: 
                bad.append(i)
                if len(bad)>2: return False
        if len(bad) == 1: return False
        if len(bad) == 0:
            if len(s)!= len(Counter(s)): return True
            return False
        if s[bad[0]] == goal[bad[1]] and s[bad[1]] == goal[bad[0]]: return True
        return False