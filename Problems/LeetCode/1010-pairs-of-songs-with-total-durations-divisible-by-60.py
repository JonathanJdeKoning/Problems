class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        fq = Counter([x%60 for x in time])
        ans = 0
        ans += (fq[30] * (fq[30] - 1)) // 2
        ans += (fq[0] * (fq[0] - 1)) // 2 
        

        for i in range(1,30):
            ans += fq[i] * fq[60 - i]
        return ans