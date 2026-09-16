class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                x = stack.pop()
                y = x*2

                stack.append(x)
                stack.append(y)
            elif op == "+":
                x = stack.pop()
                y = stack.pop()
                z = x + y

                stack.append(y)
                stack.append(x)
                stack.append(z)
            else:
                stack.append(int(op))
        
        ans = 0
        while (stack):
            ans += stack.pop()
        return ans
