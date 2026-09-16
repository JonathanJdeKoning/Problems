class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-pile for pile in gifts]
        heapify(gifts)
        for _ in range(k):
            mx = -heappop(gifts)
            heappush(gifts, -floor(sqrt(mx)))

        return -sum(gifts)

