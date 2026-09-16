class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        fq = Counter([x%k for x in arr])
        for i in range(1,k//2+1):
            if fq[i] != fq[k-i]: return False
        if fq[0]%2!=0: return False
        return True
