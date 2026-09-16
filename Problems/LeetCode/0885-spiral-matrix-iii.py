class Solution:
    def spiralMatrixIII(self, R: int, C: int, y: int, x: int) -> List[List[int]]:
        ans = [[y, x]]
        moveLen = 1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        currDir = 0
        while len(ans) != R*C:
            for _ in range(2):
                for i in range(moveLen):
                    dy,dx = directions[currDir]
                    y += dy
                    x += dx

                    if min(y,x) < 0 or y >= R or x >= C: continue
                    ans.append([y, x])
                    
                currDir = (currDir+1)%4
            moveLen+= 1
        return ans


            