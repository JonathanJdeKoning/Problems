class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        q = deque(list(s))
        for d, a in shift:
            if d == 1:
                q.rotate(a)
            else:
                q.rotate(-a)
        return "".join(q)