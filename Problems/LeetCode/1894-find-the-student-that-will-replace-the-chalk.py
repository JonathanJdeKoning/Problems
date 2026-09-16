class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, kid in enumerate(chalk):
            k -= kid
            if k < 0: return i
