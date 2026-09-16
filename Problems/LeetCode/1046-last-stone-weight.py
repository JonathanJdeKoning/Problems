class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones:
            heappush(heap, -stone)

        while len(heap) >= 2:
            y = heappop(heap)
            x = heappop(heap)
            
            if y != x:
                heappush(heap, y-x)
        
        if heap:
            return -heap[0]
        
        return 0

