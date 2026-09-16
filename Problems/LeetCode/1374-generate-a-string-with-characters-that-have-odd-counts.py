class Solution:
    def generateTheString(self, n: int) -> str:
        return "a"*n if n%2==1 else ("a"+"b"*(n-1))