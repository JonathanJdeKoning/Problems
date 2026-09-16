class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        curr = 0
        mx = 0
        best = None
        for i, t in events:
            if t-curr > mx:
                mx = t-curr
                best = i
            elif t-curr == mx:
                best = min(i, best)
            curr = t
        return best