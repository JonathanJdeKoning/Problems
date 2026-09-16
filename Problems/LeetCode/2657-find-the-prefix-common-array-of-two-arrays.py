class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        a = set()
        b = set()

        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            ans.append(len(a.intersection(b)))
        return ans