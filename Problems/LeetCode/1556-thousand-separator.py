class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = f'{n:,}'
        return s.replace(",", ".")