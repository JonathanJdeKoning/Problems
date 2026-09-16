class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        
        def consec(a,b):
            return ((ord(a)-97)+1)%26 == ((ord(b)-97))%26 or ((ord(a)-97)-1)%26 == ((ord(b)-97))%26
        for c in s:
            if not stack: 
                stack.append(c)
                continue

            if consec(c, stack[-1]):
                stack.pop()
                continue
            else:
                stack.append(c)
                
        return "".join(stack)