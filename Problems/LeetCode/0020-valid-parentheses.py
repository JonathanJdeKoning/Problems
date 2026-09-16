class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack: return False
                if stack[-1] == mp[c]:
                    stack.pop()
                else:
                    return False

        return not stack 


        