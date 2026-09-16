class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        possible = list(map(lambda x: -1 if x ==0 else 1, possible))
        total = sum(possible)
        
        daniel = possible[0]
        total -= daniel
        numgames = 1
        
        for i, game in enumerate(possible[1:-1],start = 1):
            if daniel > total: return numgames
            daniel += game
            total -= game
            numgames += 1
        if daniel > total: return numgames
        return -1
        
                