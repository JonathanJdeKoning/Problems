class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []

        for char in s:
            if sStack and char == "#":
                sStack.pop()
                continue
            if char != "#":
                sStack.append(char)
                
        for char in t:
            if tStack and char == "#":
                tStack.pop()
                continue
            if char != "#":
                tStack.append(char)

        return sStack == tStack
