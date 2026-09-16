class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trusts = {}
        for i in range(1, n+1):
            trusts[i] = {"trusts":[], "trusted_by":[]}
        
        for t in trust:
            trusts[t[0]]["trusts"].append(t[1])
            trusts[t[1]]["trusted_by"].append(t[0])
        for k, v in trusts.items():
            if not v["trusts"] and len(v["trusted_by"]) == n-1:
                return k
        return -1