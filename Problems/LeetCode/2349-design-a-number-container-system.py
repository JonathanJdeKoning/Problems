from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.numToIndex = defaultdict(SortedList)
        self.indexToNum = {}

    def change(self, index: int, number: int) -> None:
        if index in self.indexToNum:
            holder = self.indexToNum[index]
            self.numToIndex[holder].discard(index)
        self.indexToNum[index] = number
        self.numToIndex[number].add(index)

    def find(self, number: int) -> int:
        if not self.numToIndex[number]: return -1
        return self.numToIndex[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)