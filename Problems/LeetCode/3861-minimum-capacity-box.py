class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = min([x for x in capacity if x >= itemSize], default=-1)
        if ans == -1: return ans

        for i, b in enumerate(capacity):
            if b == ans:
                return i