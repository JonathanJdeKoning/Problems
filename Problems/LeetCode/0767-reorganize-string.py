class Solution:
    def reorganizeString(self, s: str) -> str:
        fq = Counter(s)
        h = []
        ans = []
        justUsed = None
        for k,v in fq.items():
            heappush(h, (-v, k))

        while h:
            count, k = heappop(h)
            ans.append(k)
            count += 1
            if justUsed is not None:
                heappush(h, justUsed)
                justUsed = None
            
            if count < 0:
                justUsed = (count, k)

        res = "".join(ans)
        if len(res) == len(s):
            return res
        return ""
                
