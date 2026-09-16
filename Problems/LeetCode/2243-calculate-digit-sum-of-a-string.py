class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = []

            for i in range(0,len(s), k):
                slc = s[i:i+k]
                groups.append(slc)
            new = []
            for i, group in enumerate(groups):
                new.append(str(sum([int(x) for x in group])))
            s = "".join([x for x in new])
        return s
        