class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        inStack = set()
        stack = []
        nextPop = 0
        nextPush = 0

        while nextPop != len(popped) or nextPush != len(pushed):
            if stack and popped[nextPop] == stack[-1]:
                inStack.discard(stack.pop())
                nextPop += 1
            elif popped[nextPop] in inStack:
                return False
            else:
                stack.append(pushed[nextPush])
                inStack.add(pushed[nextPush])
                nextPush += 1
        return True