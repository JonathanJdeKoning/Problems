class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = set()
        for i, row in enumerate(grid):
            if row.count(1) >= 2:
                for j in range(C):
                    if row[j] == 1: ans.add((i,j))

        for j in range(C):
            col = [row[j] for row in grid]
            if col.count(1) >= 2:
                for i in range(R):
                    if col[i] == 1:
                        ans.add((i,j))
        print(ans)
        return len(ans)



