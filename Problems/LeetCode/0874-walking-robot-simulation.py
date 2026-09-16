class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dy, dx = 1,0
        obstacles = set([(y,x) for y,x in obstacles])
        right = {(1,0):(0,1),(0,1):(-1,0),(-1,0):(0,-1),(0,-1):(1,0)}
        
        left = {(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1),(0,1):(1,0)}

        y,x = 0,0
        mx = 0
        for command in commands:
            if command > 0:
                for _ in range(command):
                    newY, newX = y+dy, x+dx

                    if (newX, newY) in obstacles:
                        break
                    y, x = newY, newX
                    mx = max(mx, newY**2+newX**2)
        
            elif command ==-1:
                dy,dx = right[(dy,dx)]
            else:
                dy, dx = left[(dy,dx)]
        return mx