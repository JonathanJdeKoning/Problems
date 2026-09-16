class Solution:
    def grayCode(self, n: int) -> List[int]:
        

        def gray(n):
            if n==1: return ["0", "1"]

            old = gray(n-1)
            ref = ["1" + x for x in old[::-1]]

            old = ["0" + x for x in old]

            return old+ ref
        return list(map(lambda x: int(x, 2), gray(n)))


