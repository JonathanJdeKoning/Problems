class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        new = ""
        if str(x)[0] == "-":
            neg = True
            x = int(str(x)[1:][::-1])
        else:
            x = int(str(x)[::-1])
        if neg:
            new += "-"
            new += str(x)
            new = int(new)
        else:
            new += str(x)
        new = int(new)

        if new < -2147483648 or new > 2147483647:
            return 0
        return new