class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        A = [True]*32000
        A[1] = False
        A[0] = False
        for i in range(2, len(A)):
            if A[i]:
                for j in range(i+i, len(A), i):
                    A[j] = False
        P = [i for i, x in enumerate(A) if x]
        print(P[:10])

        count = (r-l) + 1

        for p in P:
            if l <= p**2 <= r:
                count -= 1
        return count