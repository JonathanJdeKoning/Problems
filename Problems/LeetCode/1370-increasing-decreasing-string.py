class Solution:
    def sortString(self, s: str) -> str:
        out = []
        s = sorted(list(s))

        while len(s) > 0:
            toadd = sorted(list(set(s)))
            out.extend(toadd)
            for c in toadd: s.remove(c)
            toadd = sorted(list(set(s)), reverse=True)
            out.extend(toadd)
            for c in toadd: s.remove(c)
        return "".join(out)



