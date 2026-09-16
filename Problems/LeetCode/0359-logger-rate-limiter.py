class Logger:

    def __init__(self):
        self.mp = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp >= self.mp[message]:
            self.mp[message] = timestamp+10
            return True
        return False        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)