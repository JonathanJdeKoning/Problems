class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s, reverse = True)
        if not s: return 0

        currcookie = s.pop()
        total = 0
        for child in g:
            while child > currcookie:
                try:
                    currcookie = s.pop()
                except: return total
            total += 1
            try:
                currcookie = s.pop()
            except: return total
        return total
