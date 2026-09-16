class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        cols = len(grid[0])
        for row in grid:
            arr += row
        q = deque(arr)
        q.rotate(k)
        a = list(q)
        new = []
        for i in range(0, len(a),cols):
            new.append(a[i:i+cols])
        return new