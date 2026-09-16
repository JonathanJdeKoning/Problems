class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod = 1000000007
        R, C = len(grid), len(grid[0])
        
        @cache
        def ways_to_get_k(i,j,k):
            if min(i,j) == -1 or i == R or j == C:
                return 0 
            if i == 0 and j == 0:
                return 1 if grid[0][0] == k else 0 
            base = grid[i][j]
            need = base^k
            return ways_to_get_k(i-1, j, need) + ways_to_get_k(i, j-1, need)
            
        ans =  ways_to_get_k(R-1, C-1, k)%mod
        ways_to_get_k.cache_clear()
        return ans