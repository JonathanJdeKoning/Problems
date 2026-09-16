class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append("(")
                mx = max(mx, len(stack))
            if c == ")":
                stack.pop()
        return mx