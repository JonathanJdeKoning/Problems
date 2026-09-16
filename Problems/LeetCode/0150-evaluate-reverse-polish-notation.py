import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/": 
                stack.append(int(token)) 
                continue
                
            y = stack.pop()
            x = stack.pop()

            if token != "/":
                stack.append(eval(f"{x}{token}{y}"))
                continue

            num = x/y
            if num < 0:
                stack.append(int(math.ceil(num)))
            else:
                stack.append(int(math.floor(x//y)))
        return stack[0]