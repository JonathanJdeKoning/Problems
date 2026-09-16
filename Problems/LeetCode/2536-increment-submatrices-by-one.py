class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diffMat = [[0]*(n+1) for _ in range(n+1)]
        
        # diff = [[0]*(n) for _ in range(n)]
        # for r1, c1, r2, c2 in queries:
        #     diff[r1][c1] += 1
            
        
        """
         1  0 -1  0
         0  1 -1  0
        -1  1  0  0
         0  0  0  0
        1 1 0
        
        1  0  0  0
        0  1  -1  0
        0  -1  0  -1
        0  0  -1  0
        
        0 0 0 0 
        0 1 0 -1
        0 0 0 0
        0 -1 0 1
        
        
        """
        
        for i1, j1, i2, j2 in queries:
            diffMat[i1][j1] += 1
            diffMat[i2+1][j1] -= 1
            diffMat[i1][j2+1] -= 1
            diffMat[i2+1][j2+1] += 1
        
        for j in range(n+1):
            colSum = 0
            for i in range(n+1):
                colSum += diffMat[i][j]
                diffMat[i][j] = colSum
                
        for i in range(n+1):
            rowSum = 0
            for j in range(n+1):
                rowSum += diffMat[i][j]
                diffMat[i][j] = rowSum
                
        return [row[:-1] for row in diffMat[:-1]]
        
                
            
            