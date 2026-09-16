class Solution:
    def minOperations(self, k: int) -> int:
        num = ceil(sqrt(k))
        return num-1 + ceil(k/num) -1