class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = defaultdict(int)
        for dom in cpdomains:
            n, d = dom.split()
            n = int(n)
            ss = d.split(".")
            for i, s in enumerate(ss):
                c['.'.join(ss[i:])] += n

        return [f"{v} {k}" for k,v in c.items()]
    