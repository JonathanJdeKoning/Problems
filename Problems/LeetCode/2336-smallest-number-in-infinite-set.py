class SmallestInfiniteSet:

    def __init__(self):
        self.h = list(range(1,1002))
        self.s = set(range(1,1002))
        heapify(self.h)
    def popSmallest(self) -> int:
        x = heappop(self.h)
        self.s.discard(x)
        return x

    def addBack(self, num: int) -> None:
        if num not in self.s:
            self.s.add(num)
            heappush(self.h, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)