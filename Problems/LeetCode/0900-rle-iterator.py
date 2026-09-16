class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.A = encoding
        self.curr = 0

    def next(self, n: int) -> int:
        if self.curr >= len(self.A): return -1
        while self.A[self.curr] < n:
            n -= self.A[self.curr]
            self.curr += 2
            if self.curr >= len(self.A): return -1
        ans = self.A[self.curr + 1]
        self.A[self.curr] -= n
        if self.A[self.curr] == 0:
            self.curr += 2
        return ans




# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)