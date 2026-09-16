class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.i+1]

        self.i += 1
        self.hist.append(url)


    def back(self, steps: int) -> str:
        new = max(self.i - steps, 0)
        self.i = new
        return self.hist[self.i] 

    def forward(self, steps: int) -> str:
        new = min(self.i + steps, len(self.hist)-1)
        self.i = new
        return self.hist[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)