class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        new = [[None]*C for _ in range(R)]
        mid = C//2

        for x in range((-R)+1,R):
            newdiag = []
            ny = 0
            nx = x

            while True:
                if min(ny,nx) <= -1:
                    ny += 1
                    nx += 1
                    continue
                if ny >= R or nx >= C: break
                newdiag.append(grid[ny][nx])
                ny += 1
                nx += 1

            newdiag.sort()
            if x>=1:
                newdiag = newdiag[::-1]
            print(newdiag)

            ny = 0 
            nx = x
            while True:
                if min(ny,nx) <= -1:
                    ny += 1
                    nx += 1                
                    continue
                if ny >= R or nx >= C: break
                new[ny][nx] = newdiag.pop()
                ny += 1
                nx += 1
        return new