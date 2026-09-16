class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        R, C = len(mat), len(mat[0])

        for i in range(R):
            for j in range(C):
                if i != 0: mat[i][j] += mat[i-1][j]
                if j!= 0: mat[i][j] += mat[i][j-1]
                if i!= 0 and j != 0: mat[i][j] -= mat[i-1][j-1]

        for row in mat:
            print(row)

        def subSum(i,j,size):
            total = mat[i+(size-1)][j+(size-1)]

            if i != 0:total -= mat[i-1][j+(size-1)]
            if j != 0:total -= mat[i+(size-1)][j-1]
            if i != 0 and j != 0: total += mat[i-1][j-1]
            return total

        def satisfies(sideLength):
            if sideLength == 0: return True

            if sideLength > min(R,C): return False
            for i in range(R-(sideLength-1)):
                for j in range(C-(sideLength-1)):
                    if subSum(i,j, sideLength) <= threshold: return True
            return False



        low = 0
        
        high = max(R,C)+1

        while high > low + 1:
            mid = (low + high) // 2

            if satisfies(mid):
                low = mid
            else:
                high = mid
        return low