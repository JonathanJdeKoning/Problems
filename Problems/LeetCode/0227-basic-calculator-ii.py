class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        stack = []
        g = groupby(s, key=lambda x:x.isdigit())
        for k, v in g:
            if k:
                stack.append(int("".join(list(v))))
            else:
                stack.append("".join(list(v)))
        new = []

        for cell in stack:
            if type(cell) == type("") or not new:
                new.append(cell)
            else:
                op = new[-1]
                if op == "*":
                    new.pop()
                    sec = new.pop()
                    new.append( sec * cell)
                elif op == "/":
                    new.pop()
                    sec = new.pop()
                    new.append(sec // cell)
                else:
                    new.append(cell)
        base = new[0]
        for i in range(2, len(new), 2):
            op = new[i-1]
            other = new[i]
            if op == "+":
                base = base + other
            else:
                base = base - other
        return base

