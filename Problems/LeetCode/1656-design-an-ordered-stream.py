class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None]*n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        out=[]
        for c in self.arr[self.ptr:]:
            if c:
                out.append(c)
                self.ptr+=1
            else:
                return out
        return out


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)