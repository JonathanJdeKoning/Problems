class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = map(int, num1[:-1].split("+"))
        a2, b2 = map(int, num2[:-1].split("+"))
        N = complex(a1, b1) * complex(a2, b2)
        return f"{int(N.real)}+{int(N.imag)}i"
