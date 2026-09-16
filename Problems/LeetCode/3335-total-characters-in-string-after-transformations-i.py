class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        A = deque([s.count(chr(i+97)) for i in range(26)])
        for _ in range(t):
            A[0] += (zs := A.pop())
            A.appendleft(zs)
        return sum(A)%int(1e9+7)
            