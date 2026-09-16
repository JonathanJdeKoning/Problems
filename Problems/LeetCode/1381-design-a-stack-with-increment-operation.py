class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) != self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        try:
            return self.stack.pop()
        except: return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            try:
                self.stack[i] += val
            except: break


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)