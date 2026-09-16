class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        def l2w(c):
            return widths[ord(c)-97]
        
        lines = 1
        currline = 0
        for c in s:
            charwidth = l2w(c)
            if currline+charwidth <= 100:
                currline += charwidth
                continue
            else:
                lines += 1
                currline = charwidth
        return [lines, currline]

        