class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        ans = []
        for i in range(R):
            row = []
            for j in range(C):
                if (i+j)%2==0:
                    row.append(grid[i][j])
            if i%2==0:
                ans.extend(row)
            else:
                ans.extend(row[::-1])
        return ans