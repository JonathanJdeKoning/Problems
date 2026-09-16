class Solution:

    def __init__(self, w: List[int]):
        self.arr = w
        self.idx = list(range(len(w)))
        self.n = sum(w)
        self.prob = [x/self.n for x in w]

    def pickIndex(self) -> int:
        return random.choices(self.idx, self.prob)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()