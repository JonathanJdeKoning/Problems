class MyCalendar:

    def __init__(self):
        self.A = []

    def book(self, startTime: int, endTime: int) -> bool:
        for a, b in self.A:
            if startTime <= a and endTime>=b:
                return False
            if startTime > a and startTime < b:
                return False
            if endTime > a and endTime < b:
                return False
        self.A.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)