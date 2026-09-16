class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        out = []
        while a or b:
            if out[-2:] == ["a", "a"]:
                out.append("b")
                b -= 1
                continue
            if out[-2:] == ["b", "b"]:
                out.append("a")
                a -= 1
                continue
            if a >= b:
                out.append("a")
                a -= 1
            elif b > a:
                out.append("b")
                b -= 1
        return "".join(out)
            