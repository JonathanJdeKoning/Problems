class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        q = deque([(i,0) for i in skills])
        best = max(skills)
        
        while True:
            aStrength, aWins = q.popleft()
            bStrength, bWins = q.popleft()
            if aStrength == best or bStrength == best:
                return skills.index(best)
            
            if aStrength > bStrength:
                if aWins + 1 == k:
                    return skills.index(aStrength)
                
                
                q.append((bStrength, 0))
                q.appendleft((aStrength, aWins+1))
            else:
                if bWins + 1 == k:
                    return skills.index(bStrength)
                
                q.append((aStrength, 0))
                q.appendleft((bStrength, bWins+1))
            
            
        
        