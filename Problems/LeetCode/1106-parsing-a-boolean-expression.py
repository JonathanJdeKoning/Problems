class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        translation = {"f": False, "t": True}
        for c in expression.replace(",","").replace("(",""):
            if c == ")":
                e = [stack.pop() for _ in range(len(stack)) if stack[-1] not in ["!","|","&"]]
                if (op := stack.pop()) == "&": stack.append(all(e))
                elif op == "!": stack.append(not(e[0]))
                else: stack.append(any(e))
                continue
            stack.append(translation.get(c, c))
        return stack[0]