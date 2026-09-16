class StringIterator:

    def __init__(self, compressedString: str):
        g = groupby(compressedString, key = lambda x: x.isdigit())
        self.s = []
        prev = None
        for k,v in g:
            if k:
                n = int("".join(list(v)))
                self.s.append(n * prev)

            else:
                prev = list(v)[0]
        self.s = "".join(self.s)
        self.idx = 0


    def next(self) -> str:
        if self.idx == len(self.s): return  " "
        ans = self.s[self.idx]
        self.idx += 1
        return ans


    def hasNext(self) -> bool:
        return self.idx != len(self.s)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()