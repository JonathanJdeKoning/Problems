class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i,c in enumerate(columnTitle[::-1]):
            letternum = ord(c) - 64
            total += letternum*26**i
        return total
