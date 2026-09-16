class MinStack:

    def __init__(self):
        self.stack = []
        self.mnStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.mnStack or self.mnStack[-1] >= value:
            self.mnStack.append(value)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mnStack[-1]:
            self.mnStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mnStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()