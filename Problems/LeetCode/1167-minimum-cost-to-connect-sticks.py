class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        heapify(sticks)
        while len(sticks) != 1:
            x = heappop(sticks)
            y = heappop(sticks)
            ans += x + y
            heappush(sticks, x+y)
        return ans