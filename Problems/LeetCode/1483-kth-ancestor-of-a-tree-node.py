class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.up = [[] for _ in range(len(parent))]
        mxJumps = len(parent)
        bit = 1
        for i, p in enumerate(parent):
            self.up[i].append(p)
        while 2**bit <= mxJumps:
            for i in range(len(parent)):
                jump = self.up[i][bit-1]
                if jump == -1:
                    self.up[i].append(-1)
                else:
                    self.up[i].append(self.up[jump][bit-1])
            bit += 1
        print(self.up)
            


    def getKthAncestor(self, node: int, k: int) -> int:
        bit = 0
        curr = node
        while k:
            used = k & 1
            k >>= 1
            if used:
                curr = self.up[curr][bit]
            if curr == -1: return -1
            bit += 1
        return curr


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)