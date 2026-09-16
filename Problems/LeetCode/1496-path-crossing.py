class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        y = 0
        x = 0
        seen.add((y,x))

        for c in path:
            if c == "N":y-=1
            elif c == "S": y+=1
            elif c == "E":x+= 1
            elif c == "W":x-=1
            if (y,x) not in seen:
                seen.add((y,x))
            else: return True
        return False
