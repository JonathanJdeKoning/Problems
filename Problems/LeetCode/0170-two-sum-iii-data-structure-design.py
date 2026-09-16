from sortedcontainers import SortedList
class TwoSum:

    def __init__(self):
        self.fq = defaultdict(int)
        self.nums = SortedList()

    def add(self, number: int) -> None:
        if self.fq[number] != 2:
            self.nums.add(number)
            self.fq[number] += 1

    def find(self, value: int) -> bool:
        l = 0
        r = len(self.nums) - 1
        while l < r:
            v = self.nums[l] + self.nums[r]
            if v == value: return True
            elif v < value:
                l += 1
            elif v > value:
                r -= 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)