class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        t = sum(skill)
        need = t//(len(skill)//2)
        fq = Counter(skill)
        ans = 0
        print(fq)
        seen = set()
        for k,v in fq.items():
            if k in seen: continue
            inv = need-k
            seen.add(inv)

            if inv == k:
                if v%2!=0: return -1
                ans += k*k*(v//2)
                continue

            if fq[inv] != v: return -1
            ans += k*inv*v
        return ans

        