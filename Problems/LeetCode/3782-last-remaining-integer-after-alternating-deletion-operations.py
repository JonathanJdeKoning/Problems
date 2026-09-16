class Solution:
    def lastInteger(self, n: int) -> int:
        return (n-1&((1<<(m:=(n-1).bit_length())+(m&1^1))-1)//3)+1
