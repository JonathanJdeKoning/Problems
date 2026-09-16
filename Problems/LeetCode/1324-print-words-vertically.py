class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        mx = max([len(x) for x in s])
        cuh = [x.ljust(mx) for x in s]
        return ["".join(x).rstrip() for x in zip(*cuh)]
