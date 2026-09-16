class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            heappush_max(self.small, num)
        else:
            heappush(self.big, num)

        while self.small and self.big and self.small[0] > self.big[0]:
            s, b = heappop_max(self.small), heappop(self.big)
            heappush_max(self.small, b)
            heappush(self.big, s)

    def findMedian(self) -> float:
        if len(self.small) != len(self.big):
            return self.small[0]
        
        return (self.small[0] + self.big[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()