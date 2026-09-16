class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        A = [0]*length
        for l, r, n in updates:
            A[l] += n
            if r < len(A)-1:
                A[r+1] -= n
        return list(accumulate(A))