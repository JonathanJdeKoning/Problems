class Solution:
    def freqAlphabets(self, s: str) -> str:
        out = []
        for c in s:
            if c == "#":
                new = 0
                new += int(out.pop())
                new+= 10*int(out.pop())
                out.append(str(new))
            else:
                out.append(c)
        return "".join([chr(int(x)+96) for x in out])
        
