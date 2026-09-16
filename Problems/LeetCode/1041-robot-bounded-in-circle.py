class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        y = 0
        x = 0
        l = {
            (-1,0):(0,-1),
            (1,0):(0,1),
            (0,1):(-1,0),
            (0,-1):(1,0)
        }
        r = {
            (-1,0):(0,1),
            (1,0):(0,-1),
            (0,1):(1,0),
            (0,-1):(-1,0)
        }
        dy, dx = -1, 0
        for _ in range(4):
            for c in instructions:
                if c == "G":
                    y += dy
                    x += dx
                elif c == "L":
                    dy, dx = l[(dy, dx)]
                elif c == "R":
                    dy, dx = r[(dy, dx)]
        if y==0 and x == 0:
            return True
        return False