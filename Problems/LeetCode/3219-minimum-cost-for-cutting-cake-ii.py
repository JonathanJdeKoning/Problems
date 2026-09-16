class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        def minimumCostOfBreaking(X, Y, m, n):
            res = 0
            X.sort(reverse = True)
            Y.sort(reverse = True)
            hzntl = 1; vert = 1
            i = 0; j = 0
            while (i < m and j < n):
            
                if (X[i] > Y[j]):
                    res += X[i] * vert
                    hzntl += 1
                    i += 1
                
                else:
                    res += Y[j] * hzntl
                    vert += 1
                    j += 1
        
            # loop for horizontal array, if remains
            total = 0
            while (i < m):
                total += X[i]
                i += 1
            res += total * vert
        
            #loop for vertical array, if remains
            total = 0
            while (j < n):
                total += Y[j]
                j += 1
            res += total * hzntl
        
            return res
            
        # Driver program

        
        return(minimumCostOfBreaking(horizontalCut, verticalCut, m-1, n-1))
