class Solution:
    def clumsy(self, n: int) -> int:
        ev = []
        ops = ["*", "//", "+", "-"]
        for i in range(1, n+1):
            ev.append(str(n-(i-1)))
            ev.append(ops[(i-1)%4])
        s = " ".join(ev[:-1])
        print(s)
        return eval(s)