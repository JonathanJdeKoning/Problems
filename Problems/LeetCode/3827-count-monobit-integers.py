class Solution:
    def countMonobit(self, n: int) -> int:
        return len([x for x in range(n+1) if len(set(bin(x)[2:])) == 1])