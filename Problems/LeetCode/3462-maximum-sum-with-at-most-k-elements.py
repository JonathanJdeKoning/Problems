class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for i in range(len(grid)):
            row = grid[i]
            rowLimit = limits[i]
            sortedRow = sorted(row, reverse=True)

            for j in range(rowLimit):
                heappush(heap, -sortedRow[j])
        ans = 0
        for _ in range(k):
            ans += -heappop(heap)
        return ans


        