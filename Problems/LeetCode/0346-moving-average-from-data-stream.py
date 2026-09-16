class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.tot = 0
        self.stream = deque([])

    def next(self, val: int) -> float:
        if len(self.stream) < self.size:
            self.tot += val
            self.stream.append(val)
            return self.tot / len(self.stream)
        else:
            self.tot -= self.stream.popleft()
            self.tot += val
            self.stream.append(val)
            return self.tot / self.size

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)