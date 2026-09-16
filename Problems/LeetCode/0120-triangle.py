class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]

        for i in range(1, len(triangle)):
            new = []
            for j in range(i+1):
                left, right = float('inf'), float('inf')
                if j != 0:
                    left = prev[j-1]
                if j != i:
                    right = prev[j]
                new.append(triangle[i][j] + min(left, right))
            prev = new
        return min(prev)