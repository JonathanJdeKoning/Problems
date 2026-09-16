class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        l = len(s)
        poss = []
        for i in range(2**l):
            poss.append(bin(i)[2:].zfill(l))

        ans = set()

        for p in poss:
            new = []
            for i in range(l):
                if p[i] == "0":
                    new.append(s[i].lower())
                else:
                    new.append(s[i].upper())
            ans.add("".join(new))
        return list(ans)