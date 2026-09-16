class ProductOfNumbers:

    def __init__(self):
        self.hist = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.hist = [1]
            return
    
        self.hist.append(self.hist[-1]*num)

    def getProduct(self, k: int) -> int:
        if k < len(self.hist):
            return self.hist[-1] // self.hist[-(k+1)]
        return 0

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)