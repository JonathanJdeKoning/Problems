from sortedcontainers import SortedSet
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.mp = {}
        self.seen = set()
        for num in nums:
            if num in self.seen : continue
            if num not in self.mp:
                self.mp[num] = 1
            else:
                self.seen.add(num)
                del self.mp[num]


    def showFirstUnique(self) -> int:
        for k in self.mp:
            return k
        return -1

    def add(self, value: int) -> None:
        if value in self.seen: return
        if value in self.mp:
            del self.mp[value]
            self.seen.add(value)
            return
        self.mp[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)