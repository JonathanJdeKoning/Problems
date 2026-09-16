class Solution:
    def minWindow(self, s: str, t: str) -> str:
        fqT = Counter(t)
        fqS = Counter([c for c in s if c in fqT])
        if not fqS >= fqT: return ""
        if len(t) == 1: return t
        fq = Counter()
        if s[0] in fqT: fq[s[0]] = 1
        l = 0
        r = 0
        answer = s
        mnLength = len(s)


        have = set()
        if s[0] in fqT:
            fq[s[0]] = 1
        if fqT[s[0]] == 1:
            have.add(s[0])
        need = len(fqT)
        def checkValid():
            return len(have) == need

        while r <= len(s) - 2:
            if not checkValid():
                r += 1
                c = s[r]
                if c not in fqT: continue
                
                fq[c] += 1
                if fq[c] >= fqT[c]:
                    have.add(c)
            
            while checkValid():
                length = r-l+1
                if length < mnLength:
                    mnLength = length
                    answer = s[l:l+length]
                c = s[l]
                fq[c] -= 1
                if c in fqT and fq[c] < fqT[c]:
                    have.discard(c)
                l += 1
            

        return answer

