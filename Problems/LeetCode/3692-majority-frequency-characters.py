class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        fq = Counter(s)
        tot = defaultdict(int)
        let = defaultdict(list)
        mx = 0
        for k, v in fq.items():
            let[v].append(k)
            mx = max(mx, len(let[v]))

        mxfq = 0
        ans = ""
        for k,v in let.items():
            if len(v) > mx:
                ans = "".join(v)
                mxfq = fq[v[0]]
            elif len(v) == mx:
                if fq[v[0]] > mxfq:
                    mxfq = fq[v[0]]
                    ans = "".join(v)
        return ans