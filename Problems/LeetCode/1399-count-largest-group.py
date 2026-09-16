class Solution:
    def countLargestGroup(self, n: int) -> int:
        size = defaultdict(int)
        mx = 0
        for i in range(1,n+1):
            tot = sum([int(x) for x in str(i)])
            size[tot] += 1
            mx = max(mx,size[tot])
        out = 0
        for k, v in size.items():
            if v == mx: out += 1
        return out
