class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])     

        rowLeft = 0
        rowRight = R-1
        def rowcon(x):
            return matrix[x][-1] >= target

        while rowLeft < rowRight:
            mid = (rowRight+rowLeft)//2
            if rowcon(mid):
                rowRight = mid
            else:
                rowLeft = mid+1
        
        colLeft = 0
        colRight = C-1

        def colcon(x):
            return matrix[rowLeft][x] >= target
        
        while colLeft < colRight:
            mid = (colLeft+colRight)//2

            if colcon(mid):
                colRight=mid
            else:
                colLeft = mid+1
        return matrix[rowLeft][colLeft] == target

