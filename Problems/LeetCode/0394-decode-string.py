class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "[":
                stack.append("[")
                continue
            if c.isdigit():
                stack.append(c)
            if c.isalpha():
                stack.append(c)
            if c == "]":
                temp = deque([])
                while stack[-1] != "[":
                    temp.appendleft(stack.pop())
                temp = "".join(temp)
                stack.pop()
                amt = 0
                exp = 0
                while stack and stack[-1].isdigit():
                    amt += 10**exp * int(stack.pop())
                    exp += 1
                stack.append(amt * temp)

        return "".join(stack)            

            