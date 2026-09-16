class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x:bin(x)[2:][::-1],nums))
        bits = defaultdict(int)
        for num in nums:
            for i,c in enumerate(num):
                if c == "1":
                    bits[i] +=1
                else:
                    bits[i] += 0
        print(bits)
        out = []
        for key, val in sorted(bits.items()):
            if val >= k:
                out.append("1")
            else:
                out.append("0")
        print(out)
        s = "".join(out).rstrip("0")[::-1]
        if len(s) == 0: return 0
        return int(s,2)