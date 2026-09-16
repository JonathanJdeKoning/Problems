class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while True:
            if memory1 < i and memory2 < i: return [i, memory1, memory2]
            if memory1 >= memory2: memory1 -= i
            else: memory2 -= i
            i += 1
