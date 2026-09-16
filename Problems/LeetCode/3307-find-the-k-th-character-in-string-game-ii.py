class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        alph = list(range(26))

        def new(n):
            if n ==0: return 25
            else:
                return n - 1
        for c in alph:
            char = c
            ops = operations.copy()
            n = 1
            for _ in range(len(ops)):
                n*=2
            curr = k
            print(n)
            while True:
                if curr <= n//2:
                    ops.pop()
                else:
                    op = ops.pop()
                    half = n//2
                    curr = curr - half

                    if op == 1:
                        char = new(char)
                n//=2
                if n==1: break
            if char == 0: return chr(c+97)
            print(char)
                    



            

