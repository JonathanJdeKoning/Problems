class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        curr = []
        for c in target:
            x = "a"
            curr.append(x)
            ans.append("".join(curr))
            while x != c:
                x = chr(ord(x)+1)
                curr.pop()
                curr.append(x)
                ans.append("".join(curr))
        return ans
            
                