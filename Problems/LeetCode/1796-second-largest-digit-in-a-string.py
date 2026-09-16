class Solution:
    def secondHighest(self, s: str) -> int:
        digs = set()
        for c in s:
            if c.isdigit():
                digs.add(int(c))
        if len(digs) < 2: return -1
        return sorted(list(digs))[-2]