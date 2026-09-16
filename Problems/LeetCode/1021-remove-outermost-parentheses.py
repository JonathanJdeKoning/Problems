class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = []

        for c in s:
            if c == "(":
                if stack:
                    ans.append("(")
                stack.append("(")

            else:
                stack.pop()
                if stack:
                    ans.append(")")

        return "".join(ans)
