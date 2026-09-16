class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = [x for x in path.split("/") if x and x != "."]
        stack = []
        for d in dirs:
            if d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return "/"+"/".join(stack)            