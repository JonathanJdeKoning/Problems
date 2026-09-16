class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        total = 0
        R,C = len(grid), len(grid[0])
        for i in range(R-2):
            for j in range(C-2):
                top = grid[i][j:j+3]
                if sum(top)!=15 or list(filter(lambda x:x>9, top)): continue

                mid = grid[i+1][j:j+3]
                if sum(mid)!=15 or list(filter(lambda x:x>9, mid)): continue

                bot = grid[i+2][j:j+3]
                if sum(bot)!=15 or list(filter(lambda x:x>9, bot)): continue

                if len(Counter(top+mid+bot)) != 9: continue

                for k in range(3):
                    if top[k]+mid[k]+bot[k] != 15: break
                else:

                    if top[0]+mid[1]+bot[2] != 15: continue
                    if top[2] +mid[1]+ bot[0] != 15: continue
                    total += 1
                continue
        return total

                

